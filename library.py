# ============================================
# Assignment: Data Analysis with Pandas & Matplotlib
# Dataset: Bank Marketing Dataset
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Beautify plots
sns.set_style("whitegrid")

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

try:
    df = pd.read_csv("bank.csv", sep=";")
    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: bank.csv not found. Please place the dataset in the same folder.")
    exit()

# Inspect first 5 rows
print("\n📌 First 5 rows:")
print(df.head())

# Check dataset info
print("\n📌 Dataset Info:")
print(df.info())

# Check missing values
print("\n📌 Missing values per column:")
print(df.isnull().sum())

# Drop missing values (if any)
df = df.dropna()

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

# Descriptive statistics for numeric columns
print("\n📌 Descriptive Statistics:")
print(df.describe())

# Example: Average balance by marital status
avg_balance_marital = df.groupby("marital")["balance"].mean()
print("\n📌 Average balance by marital status:")
print(avg_balance_marital)

# Example: Count of clients by subscription (y)
subscription_count = df["y"].value_counts()
print("\n📌 Count of clients subscribed vs not subscribed:")
print(subscription_count)

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# 1. Line Chart: Balance over first 50 customers
plt.figure(figsize=(8,5))
plt.plot(df.index[:50], df["balance"][:50], marker="o", color="blue", label="Balance")
plt.title("Line Chart: Balance for First 50 Customers")
plt.xlabel("Customer Index")
plt.ylabel("Balance")
plt.legend()
plt.show()

# 2. Bar Chart: Average Balance by Marital Status
plt.figure(figsize=(8,5))
avg_balance_marital.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Bar Chart: Average Balance by Marital Status")
plt.xlabel("Marital Status")
plt.ylabel("Average Balance")
plt.show()

# 3. Histogram: Age Distribution
plt.figure(figsize=(8,5))
plt.hist(df["age"], bins=20, color="orange", edgecolor="black")
plt.title("Histogram: Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Age vs Balance
plt.figure(figsize=(8,5))
plt.scatter(df["age"], df["balance"], alpha=0.5, c="green")
plt.title("Scatter Plot: Age vs Balance")
plt.xlabel("Age")
plt.ylabel("Balance")
plt.show()

# -------------------------------
# Task 4: Observations
# -------------------------------

print("\n📌 Observations:")
print("- Age distribution is mostly between 30 and 50 years old.")
print("- Married clients generally have higher average balances than singles or divorced clients.")
print("- There is wide variation in balance, including some very high outliers.")
print("- Scatter plot shows no strong linear relationship between age and balance.")
print("- Bar chart helps visualize which marital group has the most financial engagement.")
