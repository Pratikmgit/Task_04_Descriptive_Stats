import pandas as pd

# Ask user for the dataset filename
filename = input("Enter dataset filename: ").strip()

try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

print("\nDescriptive Statistics using Pandas\n")

# Print numeric summary
print("Summary for numeric columns:\n")
print(df.describe())

# Summary for categorical (non-numeric) columns
print("\nSummary for non-numeric (object) columns:\n")
for column in df.columns:
    if df[column].dtype == 'object':
        print(f"Column: {column}")
        unique_count = df[column].nunique()
        most_common = df[column].value_counts().head(1)
        print(f"  Unique values: {unique_count}")
        print(f"  Most frequent: {most_common.index[0]} (Count: {most_common.iloc[0]})")
        print("-" * 50)

# Try grouped summary only for certain datasets
if "page_id" in df.columns:
    group_by_cols = ["page_id"]
    if "ad_id" in df.columns:
        group_by_cols.append("ad_id")
    
    print("\nGrouped Statistics:\n")
    try:
        numeric_cols = df.select_dtypes(include=['number']).columns
        grouped = df.groupby(group_by_cols)[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])
        print(grouped.head())
    except Exception as e:
        print(f"Error in group-by aggregation: {e}")
else:
    print("\nNote: No 'page_id' or 'ad_id' columns found. Skipping group-by analysis.")