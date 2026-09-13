# 😴 Sleep Quality Prediction Using Lifestyle Factors

An interactive **Machine Learning** web application that predicts a person's **sleep quality** using lifestyle and health-related factors such as sleep duration, stress level, physical activity, heart rate, and daily steps.

The application uses and compares predictions from **Logistic Regression** and **Random Forest Classifier** through a user-friendly **Streamlit** interface.

---

## 📖 Project Overview

Sleep quality is influenced by several daily lifestyle and health habits. This project uses supervised machine learning to classify sleep quality into three project-defined categories:

- 🔴 Poor
- 🟡 Average
- 🟢 Good

Users enter their personal, lifestyle, and health information. The application then predicts sleep quality using two trained classification models.

> **Note:** The sleep quality categories are created specifically for this project and are not official medical classifications.

---

## ✨ Features

- 🛌 Predict sleep quality using lifestyle and health-related inputs
- 🤖 Logistic Regression classification model
- 🌲 Random Forest Classifier
- 📊 Compare predictions from both models
- 🌐 Interactive Streamlit web application
- ✅ Blood pressure input validation
- ⚠️ Input range validation
- 💡 General sleep improvement suggestions
- 📈 Model evaluation using accuracy and cross-validation

---

🛠️ Tech Stack

- Python
- Pandas – Data processing
- NumPy – Numerical operations
- Scikit-learn – Machine learning and evaluation
- Streamlit – Web application
- Matplotlib – Data visualization
- Seaborn – Data visualization
- Joblib – Model saving and loading

---

## 🤖 Machine Learning Models

The project trains and evaluates two supervised classification algorithms:

1. **Logistic Regression**
2. **Random Forest Classifier**

The models use preprocessing techniques such as:

- Numerical feature scaling
- Categorical feature encoding
- Train-test splitting
- Stratified sampling
- Five-fold cross-validation

---

## 📋 Input Features

The application accepts the following inputs:

- Gender
- Age
- Occupation
- Sleep Duration
- Physical Activity Level
- Stress Level
- BMI Category
- Blood Pressure
- Heart Rate
- Daily Steps

Blood pressure should be entered in the following format:

```text
120/80


📊 Dataset

Dataset: Sleep Health and Lifestyle Dataset

The dataset contains lifestyle and health-related information, including:

- Sleep Duration
- Quality of Sleep
- Physical Activity Level
- Stress Level
- BMI Category
- Blood Pressure
- Heart Rate
- Daily Steps
- Occupation
- Gender
- Age

The dataset contains 374 records.

Target Classes

The original Quality of Sleep score is converted into three project-defined categories:

Quality of Sleep Score| Category
4–6| Poor
7–8| Average
9| Good

«Note: These categories are created specifically for this project and should not be interpreted as medical classifications.»

---



⚙️ How to Run the Project

1. Open the Project

Open the "sleep-quality-prediction" folder in Visual Studio Code.

Open the VS Code terminal and move into the project folder:

cd sleep-quality-prediction

2. Create a Virtual Environment

python -m venv .venv

3. Activate the Virtual Environment

For Windows:

.venv\Scripts\activate

After activation, the terminal should display:

(.venv)

4. Install Dependencies

pip install -r requirements.txt

5. Prepare the Dataset

Run:

python prepare_data.py

This command:

- Loads the original dataset
- Removes unnecessary columns
- Creates the sleep quality categories
- Saves the prepared dataset

The prepared dataset is saved as:

data/prepared_sleep_data.csv

6. Train the Models

Run:

python train_model.py

This command:

- Loads the prepared dataset
- Separates input features and target values
- Preprocesses numerical and categorical data
- Splits the dataset into training and testing sets
- Trains Logistic Regression
- Trains Random Forest
- Calculates model accuracy
- Displays classification reports
- Displays confusion matrices
- Performs five-fold cross-validation
- Saves the trained models

The following model files are generated:

logistic_model.pkl
random_forest_model.pkl

7. Launch the Application

Run:

streamlit run app.py

The Streamlit application will open in your browser.

If it does not open automatically, visit:

http://localhost:8501

---

🖥️ How to Use the Application

1. Open the Streamlit application.
2. Enter your personal information.
3. Fill in lifestyle details.
4. Fill in health-related details.
5. Enter blood pressure in "120/80" format.
6. Click Predict Sleep Quality.
7. View the Logistic Regression prediction.
8. View the Random Forest prediction.
9. Compare the predictions from both models.
10. Read the general sleep improvement suggestions.

The predicted category will be one of:

- Poor
- Average
- Good

---

📈 Model Evaluation

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Five-fold Cross-Validation

Model Performance

Model|  Mean Five-Fold Cross-Validation Accuracy
Logistic Regressi| 95.43%
Random Forest| 95.71%

The models achieve high accuracy on this dataset because sleep quality has strong relationships with features such as:

- Sleep Duration
- Stress Level
- Heart Rate
- Age
- Physical Activity Level

The cross-validation results provide a more reliable performance estimate than a single train-test split.

---

🔄 Project Workflow

Lifestyle and Health Inputs
            |
            ▼
   Streamlit Web Interface
            |
            ▼
      Input Validation
            |
            ▼
    Data Preprocessing
            |
            ▼
  ┌───────────────────────┐
  │                       │
  ▼                       ▼
Logistic Regression   Random Forest
  │                       │
  └───────────┬───────────┘
              ▼
   Predicted Sleep Quality
              |
              ▼
 Results and General Suggestions

---

📂 Project Structure

sleep-quality-prediction/
│
├── data/
│   ├── Sleep_Health_and_Lifestyle_Dataset.csv
│   └── prepared_sleep_data.csv
│
├── .venv/
│
├── inspect_data.py
├── eda.py
├── prepare_data.py
├── train_model.py
├── validate_model.py
├── app.py
│
├── logistic_model.pkl
├── random_forest_model.pkl
│
├── requirements.txt
└── README.md

---
### 2. User Input Form

![User Input Form](screenshots/input.png)

### 3. Prediction Results

![Prediction Results](screenshots/prediction_result.png)
---

🚀 Future Enhancements

- 📊 Add interactive analytical dashboards
- 📈 Display model evaluation metrics inside the application
- 💾 Save prediction history
- 📄 Export prediction reports as PDF
- 🌍 Add a multilingual interface
- 🧠 Train models using larger and more diverse datasets
- 🔍 Add feature importance visualizations
- 🎯 Display prediction probabilities
- ☁️ Deploy the application online
- 💡 Provide more personalized sleep recommendations

---

⚠️ Limitations

- The dataset contains only 374 records.
- The dataset may not represent the entire population.
- The target categories are project-defined.
- The model uses only the available dataset features.
- Real-world sleep quality depends on many additional factors.
- The high accuracy may be influenced by strong relationships between the input features and the target.
- The model cannot provide medical diagnoses.
- The application should not replace professional medical advice.

---

⚠️ Disclaimer

This project is developed for educational and demonstration purposes only.

The predictions generated by this application are not medical advice and should not be considered a medical diagnosis or treatment recommendation.

Users should consult a qualified healthcare professional for health-related concerns.

---

👩‍💻 Author

Varshini Samireddi

GitHub:
https://github.com/varshinisamireddi114

LinkedIn:
https://www.linkedin.com/in/varshini-samireddi-21623832a