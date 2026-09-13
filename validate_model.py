import pandas as pd

# Load the original dataset
df = pd.read_csv("data/Sleep_Health_and_Lifestyle_Dataset.csv")

print("Gender values:")
print(df["Gender"].unique())

print("\nOccupation values:")
print(df["Occupation"].unique())

print("\nBMI Category values:")
print(df["BMI Category"].unique())

print("\nBlood Pressure examples:")
print(df["Blood Pressure"].unique()[:20])