import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set this to your actual CSV file name
filename = "2024_fb_ads_president_scored_anon.csv"

# Load the data
df = pd.read_csv(filename)

# Create a folder to save plots
plot_dir = "plots"
os.makedirs(plot_dir, exist_ok=True)

# Plot histograms for numeric columns
numeric_cols = df.select_dtypes(include=["number"]).columns
for col in numeric_cols:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col].dropna(), bins=30, kde=True)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/hist_{col}.png")
    plt.close()

# Bar plots for categorical columns with few unique values
object_cols = df.select_dtypes(include=["object"]).columns
for col in object_cols:
    if df[col].nunique() < 15:
        plt.figure(figsize=(8, 5))
        df[col].value_counts().plot(kind="bar")
        plt.title(f"Bar Chart of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(f"{plot_dir}/bar_{col}.png")
        plt.close()

print(f"\nAll plots saved to the '{plot_dir}' folder.")
