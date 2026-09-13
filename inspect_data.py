import pandas as pd
from pathlib import Path

# Find the CSV file inside the data folder
csv_files = list(Path("data").glob("*.csv"))

# Check whether a CSV file exists
if not csv_files:
    print("No CSV file found inside the data folder.")

else:
    # Read the dataset
    df = pd.read_csv(csv_files[0])

    print("Dataset loaded successfully!")
    print()

    # Number of rows and columns
    print("Number of rows and columns:")
    print(df.shape)
    print()

    # Column names
    print("Column names:")
    print(df.columns.tolist())
    print()

    # First 5 rows
    print("First 5 rows:")
    print(df.head())

    # -----------------------------------
    # DATASET INSPECTION
    # -----------------------------------

    print("\n" + "=" * 40)
    print("DATASET INFORMATION")
    print("=" * 40)

    # 1. Check missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    # 2. Check duplicate rows
    print("\nNumber of duplicate rows:")
    print(df.duplicated().sum())

    # 3. Check sleep-quality scores
    print("\nSleep-quality scores:")
    print(df["Quality of Sleep"].value_counts().sort_index())

    # 4. Minimum sleep-quality score
    print("\nMinimum sleep-quality score:")
    print(df["Quality of Sleep"].min())

    # 5. Maximum sleep-quality score
    print("\nMaximum sleep-quality score:")
    print(df["Quality of Sleep"].max())