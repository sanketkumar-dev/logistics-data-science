"""
Task 1: Data Collection and Cleaning - DataCo Smart Supply Chain dataset

Steps: load -> audit -> clean -> validate -> save.
Change INPUT_PATH if you run this locally or in Kaggle with a different path.
"""
import pandas as pd

# ---------- 1. Load ----------
INPUT_PATH = "data/DataCoSupplyChainDataset.csv"
OUTPUT_PATH = "data/dataco_cleaned.csv"

# latin-1 because the file contains special characters
df = pd.read_csv(INPUT_PATH, encoding="latin-1")
print("Shape:", df.shape)
print(df.head())
df.info()

# ---------- 2. Audit ----------
print("Duplicate rows:", df.duplicated().sum())
missing = (df.isnull().sum() / len(df) * 100).round(2)
print("Missing % per column:\n", missing[missing > 0])

# ---------- 3. Clean ----------
df_clean = df.copy()

# Duplicates (0 found, kept as a safety step)
df_clean = df_clean.drop_duplicates()

# Drop empty columns and columns not needed for analysis (privacy)
df_clean = df_clean.drop(columns=[
    "Product Description", "Order Zipcode",      # empty / 86% missing
    "Customer Email", "Customer Password",       # private data
    "Product Image",                             # only URLs
])

# Few missing values
df_clean["Customer Lname"] = df_clean["Customer Lname"].fillna("Unknown")
df_clean = df_clean.dropna(subset=["Customer Zipcode"])   # only 3 rows

# Strip extra spaces from text columns
for col in df_clean.columns:
    if pd.api.types.is_string_dtype(df_clean[col]):
        df_clean[col] = df_clean[col].str.strip()

# Convert text dates to datetime
fmt = "%m/%d/%Y %H:%M"
df_clean["order date (DateOrders)"] = pd.to_datetime(df_clean["order date (DateOrders)"], format=fmt)
df_clean["shipping date (DateOrders)"] = pd.to_datetime(df_clean["shipping date (DateOrders)"], format=fmt)

# Standardize column names
df_clean.columns = (df_clean.columns.str.strip().str.lower()
                    .str.replace(r"[^a-z0-9]+", "_", regex=True).str.strip("_"))

# ---------- 4. Validate ----------
print("Shape before:", df.shape, "| after:", df_clean.shape)
print("Remaining missing values:", df_clean.isnull().sum().sum())
print("Negative sales:", (df_clean["sales"] < 0).sum())
print("Zero quantity:", (df_clean["order_item_quantity"] <= 0).sum())
print("Shipping date before order date:",
      (df_clean["shipping_date_dateorders"] < df_clean["order_date_dateorders"]).sum())
late_wrong = df_clean[(df_clean["delivery_status"] == "Late delivery") &
                      (df_clean["days_for_shipping_real"] <= df_clean["days_for_shipment_scheduled"])]
print("Late delivery but not actually late:", len(late_wrong))
print(df_clean["delivery_status"].value_counts())

# ---------- 5. Save ----------
df_clean.to_csv(OUTPUT_PATH, index=False)
print("Saved:", OUTPUT_PATH)
