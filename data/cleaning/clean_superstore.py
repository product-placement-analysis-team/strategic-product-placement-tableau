import pandas as pd

RAW_PATH = "data/raw/Superstore.csv"
CLEAN_PATH = "data/cleaned/superstore_cleaned.csv"

try:
    df = pd.read_csv(RAW_PATH, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(RAW_PATH, encoding="latin-1")

before_rows = len(df)

df.columns = df.columns.str.strip()

for c in df.select_dtypes(include="object").columns:
    df[c] = df[c].astype(str).str.strip()

for c in df.columns:
    if "date" in c.lower():
        df[c] = pd.to_datetime(df[c], errors="coerce")

for c in ["Sales", "Profit", "Quantity", "Discount"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

df = df.drop_duplicates()

critical = [c for c in ["Order Date", "Product Name", "Sales", "Profit"] if c in df.columns]
if critical:
    df = df.dropna(subset=critical)

if "Order Date" in df.columns:
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month_name()

after_rows = len(df)

df.to_csv(CLEAN_PATH, index=False)

print("Before rows:", before_rows)
print("After rows :", after_rows)
print("Saved to   :", CLEAN_PATH)