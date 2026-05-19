import sqlite3
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# Create database connection
conn = sqlite3.connect("customer_data.db")

# Store dataframe as SQL table
df.to_sql("customers", conn, if_exists="replace", index=False)

cursor = conn.cursor()

# -------------------------------
# Business Questions
# -------------------------------

# 1. Total Revenue
query1 = "SELECT SUM(total_purchase_amount) FROM customers;"
print("Total Revenue:")
print(cursor.execute(query1).fetchone())

# 2. Average Customer Age
query2 = "SELECT AVG(age) FROM customers;"
print("\nAverage Customer Age:")
print(cursor.execute(query2).fetchone())

# 3. Revenue by Country
query3 = """
SELECT country, SUM(total_purchase_amount) 
FROM customers 
GROUP BY country;
"""
print("\nRevenue by Country:")
for row in cursor.execute(query3):
    print(row)

# 4. Highest Spending Customer
query4 = """
SELECT customer_id, MAX(total_purchase_amount)
FROM customers;
"""
print("\nHighest Spending Customer:")
print(cursor.execute(query4).fetchone())

conn.close()
