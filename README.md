# Logistics Data Science Analyst Internship

Virtual internship project (YuvaIntern, Nov-Dec 2026) using the public
[DataCo Smart Supply Chain](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)
dataset (180,519 rows, 53 columns).

## Task 1: Data Collection and Cleaning
**Goal:** load a public logistics dataset, find data quality problems, clean them, and validate the result.

**What I did**
- Loaded the CSV with pandas (`encoding="latin-1"`)
- Audited duplicates, missing values and data types
- Dropped empty and private columns, handled few missing values, converted text dates to datetime, standardized column names
- Validated logic (no negative sales, no shipping before order date, delivery status consistent with days)

**Result:** 180,519 rows / 53 columns -> 180,516 rows / 48 columns, 0 missing values.

**Key findings**
- 0 duplicate rows
- `Product Description` 100% empty, `Order Zipcode` 86% missing
- About 54.8% of orders were late deliveries

## Files
- `task1_cleaning/data_cleaning.py` - full cleaning script
- `task1_cleaning/` - notebook (.ipynb) exported from Kaggle
- `reports/Task1_Data_Cleaning_Report.docx` - report

> The full dataset and cleaned CSV are not uploaded because of their size. Download the dataset from the Kaggle link above.

## Tools
Python, pandas, Kaggle Notebooks

## Next
Task 2: Exploratory Data Analysis (EDA)
