import polars as pl

# Ask user for the dataset filename
filename = input("Enter dataset filename: ").strip()

if not filename.endswith(".csv"):
    filename += ".csv"

try:
    df = pl.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

print("\nDescriptive Statistics using Polars\n")

# Numeric summary
numeric_cols = [col for col in df.columns if pl.datatypes.is_numeric(df[col].dtype)]
if numeric_cols:
    print("Summary for numeric columns:\n")
    print(df.select(numeric_cols).describe())

# Summary for string columns
print("\nSummary for non-numeric (string) columns:\n")
for col in df.columns:
    if df[col].dtype == pl.Utf8:
        unique_vals = df.select(pl.col(col).n_unique()).item()
        value_counts = df.select(pl.col(col).value_counts()).to_dict(as_series=False)[col]
        if value_counts:
            most_common = value_counts[0]
            print(f"Column: {col}")
            print(f"  Unique values: {unique_vals}")
            print(f"  Most frequent: {most_common['value']} (Count: {most_common['counts']})")
            print("-" * 50)

# Grouped summary
if "page_id" in df.columns:
    group_cols = ["page_id"]
    if "ad_id" in df.columns:
        group_cols.append("ad_id")

    try:
        print("\nGrouped Statistics:\n")
        stats_df = (
            df.groupby(group_cols)
              .agg([pl.col(col).mean().alias(f"{col}_mean") for col in numeric_cols])
        )
        print(stats_df.head(5))
    except Exception as e:
        print(f"Error in group-by aggregation: {e}")
else:
    print("\nNote: No 'page_id' or 'ad_id' columns found. Skipping group-by analysis.")
