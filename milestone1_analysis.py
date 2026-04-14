import pandas as pd
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt

df = pd.read_excel("online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df.dropna()

df = df[df["Quantity"] > 0]
df = df[df["Price"] > 0]

df["TotalPrice"] = df["Quantity"] * df["Price"]

print(df.head())
customer_df = df.groupby("Customer ID").agg({
    "Invoice": "nunique",
    "TotalPrice": "sum"
}).reset_index()

customer_df.columns = ["CustomerID", "Frequency", "Monetary"]

print(customer_df.head())
threshold = customer_df["Monetary"].quantile(0.80)

customer_df["HighValue"] = (customer_df["Monetary"] >= threshold).astype(int)

print(customer_df["HighValue"].value_counts())

high_freq = customer_df[customer_df["HighValue"] == 1]["Frequency"]
low_freq = customer_df[customer_df["HighValue"] == 0]["Frequency"]

stat, p_value = mannwhitneyu(high_freq, low_freq)

print(p_value)

plt.hist(customer_df["Frequency"])
plt.show()


high_freq = customer_df[customer_df["HighValue"] == 1]["Frequency"]
low_freq = customer_df[customer_df["HighValue"] == 0]["Frequency"]

stat, p_value = mannwhitneyu(high_freq, low_freq)

print("p-value:", p_value)
customer_df.to_csv("data/processed_data.csv", index=False)

