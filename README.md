# Task 04 – Descriptive Statistics

## Overview

This project focuses on analyzing real-world political social media data using descriptive statistics. The data comes from the 2024 U.S. presidential election and includes Facebook ads, Facebook posts, and Twitter posts.

The same analysis is done using:
- Pure Python (no external libraries)
- Pandas
- Polars

Each script summarizes the data (like mean, count, unique values) and optionally groups it by relevant fields like `page_id` or `ad_id`.

## Files in This Folder

- `pure_python_stats.py` – runs summary statistics using only Python’s built-in tools  
- `pandas_stats.py` – uses pandas for easy numeric and categorical summaries  
- `polars_stats.py` – uses polars for fast operations on large files  
- `visualizations.py` – creates histograms and bar plots for all 3 datasets  
- `plots/` – auto-created folder where visualizations are saved  
- `.gitignore` – used to exclude CSV data files from being pushed to GitHub  

## Datasets Used

These are large CSV files placed in this same folder:
- `2024_fb_ads_president_scored_anon.csv`
- `2024_fb_posts_president_scored_anon.csv`
- `2024_tw_posts_president_scored_anon.csv`

**Note:** These files are not included in the GitHub repo.

## How to Run the Scripts

1. Open the terminal inside this folder.
2. Run a script:
   ```bash
   python pandas_stats.py
   ```
3. When prompted, type the filename (like `2024_fb_posts_president_scored_anon.csv`)
4. To generate charts, run:
   ```bash
   python visualizations.py
   ```

Charts will be saved automatically inside the `plots/` folder.

## Summary

This task helped compare how easy or hard it is to run descriptive stats using different tools. Pandas was the most straightforward. Polars was fast and clean but had a steeper learning curve. Pure Python took the most code and effort.
