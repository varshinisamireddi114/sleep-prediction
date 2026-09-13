import pandas as pd


# Load the original dataset
df = pd.read_csv("data/Sleep_Health_and_Lifestyle_Dataset.csv")


# Remove unnecessary columns
df = df.drop(columns=["Person ID", "Sleep Disorder"])


# Convert numerical sleep quality into project-defined categories
#
# Important:
# These categories are created specifically for this project.
# They are not official medical classifications.
#
# Quality of Sleep score:
# 4–6  -> Poor
# 7–8  -> Average
# 9    -> Good

def categorize_sleep_quality(score):
    if score <= 6:
        return "Poor"
    elif score <= 8:
        return "Average"
    else:
        return "Good"


# Create the target category column
df["Sleep Quality Category"] = df["Quality of Sleep"].apply(
    categorize_sleep_quality
)


# Separate input features and target
X = df.drop(
    columns=["Quality of Sleep", "Sleep Quality Category"]
)

y = df["Sleep Quality Category"]


# Save the prepared dataset
df.to_csv(
    "data/prepared_sleep_data.csv",
    index=False
)


# Display preparation details
print("Prepared dataset saved successfully!")

print("\nSleep quality category rules:")
print("Quality of Sleep 4–6  -> Poor")
print("Quality of Sleep 7–8  -> Average")
print("Quality of Sleep 9    -> Good")
print("These are project-defined categories, not medical classifications.")

print("\nCategory distribution:")
print(y.value_counts())

print("\nInput features:")
print(X.columns.tolist())

print("\nTarget:")
print(y.name)

print("\nInput shape:")
print(X.shape)

print("\nTarget shape:")
print(y.shape)