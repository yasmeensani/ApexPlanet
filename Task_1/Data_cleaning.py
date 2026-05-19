import pandas as pd
df = pd.read_csv("C:\Users\Kota Likhitha lakshm\OneDrive\Documents\raw_data.csv")

print("Initial Shape:", df.shape)
print(df.head())

# 2. Data Quality Assessment

print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nData Types:\n", df.dtypes)
print("\nStatistical Summary:\n", df.describe())

# 3. Remove duplicates

df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)

# 4. Handle missing values

df["order_amount"] = df["order_amount"].fillna(df["order_amount"].median())

df["date_of_birth"] = pd.to_datetime(df["date_of_birth"], errors="coerce")
df["date_of_birth"] = df["date_of_birth"].fillna(pd.Timestamp("1990-01-01"))

# 5. Standardize gender column

df["gender"] = df["gender"].str.lower().str.strip()
df["gender"] = df["gender"].replace({
    "m": "male",
    "f": "female"
})

# 6. Fix date formats

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# 7. Feature Engineering

today = pd.to_datetime("today")
df["customer_age"] = (today - df["date_of_birth"]).dt.days // 365


df["order_month"] = df["order_date"].dt.month
df["order_year"] = df["order_date"].dt.year

# 8. Handle outliers

upper_limit = df["order_amount"].quantile(0.95)
df["order_amount"] = df["order_amount"].clip(upper=upper_limit)

# 9. Final check

print("\nFinal Dataset Info:")
print(df.info())

# 10. Export cleaned dataset

df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned dataset saved as cleaned_data.csv")