# Data Immersion & Wrangling

## Project Overview
This project focuses on data immersion, profiling, cleaning, transformation, and feature engineering to prepare raw business data for analysis. The goal is to identify data quality issues, improve data consistency, and generate a final analysis-ready dataset.

The project simulates a real-world data preprocessing workflow commonly used in analytics and data science projects.

---

# Objectives

- Understand the dataset structure and business context
- Create a detailed data dictionary
- Identify data quality issues
- Clean and preprocess raw data
- Standardize inconsistent formats
- Handle missing values and duplicates
- Detect and treat outliers
- Perform feature engineering
- Generate a clean dataset ready for analysis

---

# Data Profiling

Initial profiling was conducted to evaluate the overall quality of the dataset.

## Issues Identified
- Missing values
- Duplicate records
- Inconsistent date formats
- Incorrect data types
- Inconsistent text formatting
- Outliers in numerical columns
- Invalid category values

---

# Data Cleaning Process

## Missing Value Handling
- Numerical columns filled using mean/median values
- Categorical columns filled using mode or default labels

## Duplicate Removal
- Exact duplicate rows removed
- Redundant records cleaned

## Data Standardization
- Date formats standardized
- Text fields converted to consistent casing
- Extra spaces removed
- Categories normalized

## Outlier Treatment
Outliers were identified using:
- IQR Method
- Z-Score Analysis

Extreme values were treated appropriately to improve data quality.

---

# Feature Engineering

New business-relevant features were created, including:
- Customer Age from Date of Birth
- Revenue Categories
- Transaction Month
- Customer Tenure

These features improve analytical insights and reporting capabilities.

---

# Final Output

The final dataset is:
- Cleaned
- Structured
- Consistent
- Analysis-ready

---

# Deliverables

## GitHub Repository
- Data Dictionary
- Cleaning Scripts
- Profiling Notebook
- Cleaned Dataset
- Documentation

## LinkedIn Video
A 3–5 minute walkthrough covering:
- Dataset overview
- Data quality issues
- Cleaning process
- Feature engineering
- Final dataset output

---

# Tools & Technologies

- Python
- Pandas
- NumPy
- Jupyter Notebook

---
