import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# -------------------------------
# 1. Basic Information
# -------------------------------

print("Dataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -------------------------------
# 2. Numerical Analysis
# -------------------------------

# Age Distribution
plt.hist(df['age'])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Total Purchase Distribution
plt.hist(df['total_purchase_amount'])
plt.title("Revenue by country")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()

# -------------------------------
# 3. Categorical Analysis
# -------------------------------

print("\nGender Distribution:")
print(df['gender'].value_counts())

print("\nCountry Distribution:")
print(df['country'].value_counts())

df['gender'].value_counts().plot(kind='bar')
plt.title("Gender Distribution")
plt.show()

df['country'].value_counts().plot(kind='bar')
plt.title("Country Distribution")
plt.show()


import seaborn as sns

# -------------------------------
# 4. Correlation Analysis
# -------------------------------

print("\nCorrelation Matrix:")
print(df.select_dtypes(include=['number']).corr())

# Heatmap
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()


# -------------------------------
# 5. Age vs Purchase Scatter Plot
# -------------------------------

plt.scatter(df['age'], df['total_purchase_amount'])
plt.xlabel("Age")
plt.ylabel("Total Purchase Amount")
plt.title("Age vs Total Purchase Amount")
plt.show()
