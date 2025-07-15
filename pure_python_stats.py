import csv
import math
from collections import defaultdict, Counter

# Ask user to input the dataset filename
filename = input("Enter dataset filename: ").strip()

# Check if a value can be safely converted to float
def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

# Compute basic statistics for numeric columns
def compute_stats(values):
    count = len(values)
    if count == 0:
        return {"count": 0, "mean": None, "min": None, "max": None, "std_dev": None}
    
    mean = sum(values) / count
    std = math.sqrt(sum((x - mean) ** 2 for x in values) / count)
    
    return {
        "count": count,
        "mean": round(mean, 2),
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "std_dev": round(std, 2)
    }

# Read the dataset and collect column-wise data
column_data = defaultdict(list)

try:
    with open(filename, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for column, value in row.items():
                value = value.strip()
                if value == "":
                    continue
                if is_float(value):
                    column_data[column].append(float(value))
                else:
                    column_data[column].append(value)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

# Print the descriptive statistics for each column
print("\nDescriptive Statistics (Pure Python Only)\n")

for column, values in column_data.items():
    print(f"Column: {column}")
    
    if all(isinstance(v, float) for v in values):
        stats = compute_stats(values)
        for stat_name, stat_value in stats.items():
            print(f"  {stat_name}: {stat_value}")
    else:
        unique_values = set(values)
        most_common = Counter(values).most_common(1)[0]
        print(f"  Unique values: {len(unique_values)}")
        print(f"  Most frequent: {most_common[0]} (Count: {most_common[1]})")
    
    print("-" * 50)
