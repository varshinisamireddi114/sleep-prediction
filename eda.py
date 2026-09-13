import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Find only the original dataset
csv_files = list(
    Path("data").glob("Sleep_Health_and_Lifestyle_Dataset.csv")
)

# Load the dataset
df = pd.read_csv(csv_files[0])

print("Dataset loaded successfully!")

print("\nStatistical summary:")
print(df.describe())

print("\nUnique values in categorical columns:")

print("\nGender:")
print(df["Gender"].unique())

print("\nOccupation:")
print(df["Occupation"].unique())

print("\nBMI Category:")
print(df["BMI Category"].unique())

print("\nSleep Disorder:")
print(df["Sleep Disorder"].unique())


# Plot the distribution of sleep quality
plt.figure(figsize=(8, 5))

df["Quality of Sleep"].value_counts().sort_index().plot(kind="bar")

plt.title("Distribution of Sleep Quality")
plt.xlabel("Quality of Sleep")
plt.ylabel("Number of People")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# Plot sleep duration versus quality of sleep
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Sleep Duration"],
    df["Quality of Sleep"]
)

plt.title("Sleep Duration vs Quality of Sleep")
plt.xlabel("Sleep Duration (hours)")
plt.ylabel("Quality of Sleep")

plt.tight_layout()
plt.show()


# Person ID is an identifier and should not be used as a model feature

# Check correlations with Quality of Sleep
print("\nCorrelation with Quality of Sleep:")

numeric_columns = df.select_dtypes(include=["number"])

correlations = numeric_columns.corr()["Quality of Sleep"].sort_values(
    ascending=False
)

print(correlations)