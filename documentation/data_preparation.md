# Data Preparation Documentation

## Cleaning Steps Performed

- Removed duplicate rows
- Trimmed extra spaces from text fields
- Converted date columns to proper datetime format
- Converted Sales, Profit, Quantity, Discount to numeric
- Removed rows with missing Order Date, Product Name, Sales, or Profit
- Added derived columns: Year and Month

## Row Count Comparison

Before Cleaning: XXXX  
After Cleaning: YYYY  

## Output

Cleaned dataset saved to:
data/cleaned/superstore_cleaned.csv