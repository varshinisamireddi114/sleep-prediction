import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# Load the prepared dataset
df = pd.read_csv("data/prepared_sleep_data.csv")


# Separate input features and target
X = df.drop(columns=["Quality of Sleep", "Sleep Quality Category"])
y = df["Sleep Quality Category"]


# Identify categorical and numerical columns
categorical_columns = X.select_dtypes(include=["object"]).columns
numerical_columns = X.select_dtypes(exclude=["object"]).columns


# Create preprocessing pipeline
def create_preprocessor():
    return ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_columns
            ),
            (
                "numerical",
                StandardScaler(),
                numerical_columns
            )
        ]
    )


# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create Logistic Regression model
logistic_model = Pipeline(
    steps=[
        ("preprocessor", create_preprocessor()),
        (
            "classifier",
            LogisticRegression(max_iter=3000)
        )
    ]
)


# Train Logistic Regression
logistic_model.fit(X_train, y_train)

logistic_predictions = logistic_model.predict(X_test)


print("=" * 60)
print("LOGISTIC REGRESSION RESULTS")
print("=" * 60)

print(
    "Accuracy:",
    accuracy_score(y_test, logistic_predictions)
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        logistic_predictions,
        zero_division=0
    )
)

print("Confusion Matrix:")
print(
    confusion_matrix(
        y_test,
        logistic_predictions
    )
)


# Logistic Regression cross-validation
logistic_cv_scores = cross_val_score(
    logistic_model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

print("\n5-Fold Cross-Validation Scores:")
print(logistic_cv_scores)

print(
    "Mean Cross-Validation Accuracy:",
    logistic_cv_scores.mean()
)


# Create Random Forest model
random_forest_model = Pipeline(
    steps=[
        ("preprocessor", create_preprocessor()),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)


# Train Random Forest
random_forest_model.fit(X_train, y_train)

random_forest_predictions = random_forest_model.predict(X_test)


print("\n" + "=" * 60)
print("RANDOM FOREST RESULTS")
print("=" * 60)

print(
    "Accuracy:",
    accuracy_score(y_test, random_forest_predictions)
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        random_forest_predictions,
        zero_division=0
    )
)

print("Confusion Matrix:")
print(
    confusion_matrix(
        y_test,
        random_forest_predictions
    )
)


# Random Forest cross-validation
random_forest_cv_scores = cross_val_score(
    random_forest_model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

print("\n5-Fold Cross-Validation Scores:")
print(random_forest_cv_scores)

print(
    "Mean Cross-Validation Accuracy:",
    random_forest_cv_scores.mean()
)


# Save the trained models
joblib.dump(
    logistic_model,
    "logistic_model.pkl"
)

joblib.dump(
    random_forest_model,
    "random_forest_model.pkl"
)


print("\nModels saved successfully!")