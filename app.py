import streamlit as st
import pandas as pd
import joblib
import re


# --------------------------------------------------
# Load trained models
# --------------------------------------------------

model_one = joblib.load("logistic_model.pkl")
model_two = joblib.load("random_forest_model.pkl")


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Sleep Quality Dashboard",
    page_icon="😴",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown(
    """
    <style>
        .stApp {
            background-color: #f4f6f9;
        }

        .block-container {
            max-width: 100%;
            padding: 2rem 5rem 4rem 5rem;
        }

        /* Header */
        .dashboard-header {
            background-color: #1f2937;
            padding: 38px 45px;
            border-radius: 14px;
            margin-bottom: 35px;
        }

        .dashboard-title {
            color: white !important;
            font-size: 48px !important;
            font-weight: 800 !important;
            line-height: 1.3 !important;
        }

        .dashboard-subtitle {
            color: #e5e7eb !important;
            font-size: 23px !important;
            margin-top: 15px;
            line-height: 1.5 !important;
        }

        /* Section cards */
        .section-card {
            background-color: white;
            padding: 32px;
            border-radius: 14px;
            border: 1px solid #d1d5db;
            margin-bottom: 30px;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.06);
        }

        .section-heading {
            color: #111827 !important;
            font-size: 34px !important;
            font-weight: 800 !important;
            border-bottom: 2px solid #d1d5db;
            padding-bottom: 16px;
            margin-bottom: 28px;
            line-height: 1.4 !important;
        }

        /* All input labels */
        [data-testid="stWidgetLabel"] p {
            color: #111827 !important;
            font-size: 23px !important;
            font-weight: 700 !important;
            line-height: 1.5 !important;
        }

        label {
            color: #111827 !important;
            font-size: 23px !important;
            font-weight: 700 !important;
        }

        /* Input boxes */
        input,
        textarea {
            background-color: white !important;
            color: #111827 !important;
            border: 2px solid #9ca3af !important;
            border-radius: 8px !important;
            font-size: 22px !important;
            min-height: 52px !important;
        }

        input::placeholder {
            color: #6b7280 !important;
            font-size: 20px !important;
        }

        /* Select boxes */
        div[data-baseweb="select"] > div {
            background-color: white !important;
            border: 2px solid #9ca3af !important;
            border-radius: 8px !important;
            min-height: 52px !important;
        }

        div[data-baseweb="select"] span {
            color: #111827 !important;
            font-size: 21px !important;
        }

        /* Slider text */
        [data-testid="stSlider"] label p {
            color: #111827 !important;
            font-size: 23px !important;
            font-weight: 700 !important;
        }

        [data-testid="stSlider"] [data-testid="stTickBarMin"],
        [data-testid="stSlider"] [data-testid="stTickBarMax"] {
            font-size: 18px !important;
        }

        /* Button */
        .stButton > button {
            width: 100%;
            background-color: #2563eb;
            color: white;
            border: none;
            border-radius: 10px;
            min-height: 65px;
            font-size: 25px !important;
            font-weight: 800 !important;
        }

        .stButton > button:hover {
            background-color: #1d4ed8;
            color: white;
        }

        /* Result */
        .result-card {
            background-color: #111827;
            border-radius: 16px;
            padding: 45px;
            text-align: center;
            margin-top: 35px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
        }

        .result-label {
            color: #d1d5db !important;
            font-size: 30px !important;
            font-weight: 600 !important;
            margin-bottom: 18px;
        }

        .result-value {
            color: white !important;
            font-size: 64px !important;
            font-weight: 900 !important;
        }

        /* Suggestion */
        .suggestion-card {
            background-color: white;
            border-left: 8px solid #2563eb;
            border-radius: 12px;
            padding: 30px;
            margin-top: 28px;
            color: #111827 !important;
            font-size: 23px !important;
            line-height: 1.8 !important;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.06);
        }

        .footer-note {
            text-align: center;
            color: #4b5563 !important;
            font-size: 19px !important;
            margin-top: 35px;
        }

        /* Messages */
        .stWarning,
        .stError,
        .stSuccess,
        .stInfo {
            font-size: 21px !important;
        }

        /* Help text */
        [data-testid="stInputHelp"] {
            font-size: 18px !important;
        }

        hr {
            border: 1px solid #d1d5db;
            margin: 38px 0;
        }

        footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    """
    <div class="dashboard-header">
        <div class="dashboard-title">😴 Sleep Quality Dashboard</div>
        <div class="dashboard-subtitle">
            Enter your lifestyle and health details to predict your sleep quality.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Personal information
# --------------------------------------------------

st.markdown(
    """
    <div class="section-card">
        <div class="section-heading">👤 Personal Information</div>
    """,
    unsafe_allow_html=True
)

personal_col1, personal_col2, personal_col3 = st.columns(3)

with personal_col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with personal_col2:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25,
        step=1
    )

with personal_col3:
    occupation = st.selectbox(
        "Occupation",
        [
            "Software Engineer",
            "Doctor",
            "Sales Representative",
            "Teacher",
            "Nurse",
            "Engineer",
            "Accountant",
            "Scientist",
            "Lawyer",
            "Salesperson",
            "Manager"
        ]
    )

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# Lifestyle information
# --------------------------------------------------

st.markdown(
    """
    <div class="section-card">
        <div class="section-heading">🌿 Lifestyle Information</div>
    """,
    unsafe_allow_html=True
)

lifestyle_col1, lifestyle_col2, lifestyle_col3 = st.columns(3)

with lifestyle_col1:
    sleep_duration = st.number_input(
        "Sleep Duration (hours)",
        min_value=1.0,
        max_value=15.0,
        value=7.0,
        step=0.1
    )

with lifestyle_col2:
    physical_activity = st.number_input(
        "Physical Activity Level",
        min_value=0,
        max_value=200,
        value=60,
        step=1
    )

with lifestyle_col3:
    daily_steps = st.number_input(
        "Daily Steps",
        min_value=0,
        max_value=50000,
        value=6000,
        step=500
    )

stress_level = st.slider(
    "Stress Level",
    min_value=1,
    max_value=10,
    value=5
)

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# Health information
# --------------------------------------------------

st.markdown(
    """
    <div class="section-card">
        <div class="section-heading">❤️ Health Information</div>
    """,
    unsafe_allow_html=True
)

health_col1, health_col2, health_col3 = st.columns(3)

with health_col1:
    bmi_category = st.selectbox(
        "BMI Category",
        [
            "Normal",
            "Normal Weight",
            "Overweight",
            "Obese"
        ]
    )

with health_col2:
    heart_rate = st.number_input(
        "Heart Rate",
        min_value=40,
        max_value=150,
        value=75,
        step=1
    )

with health_col3:
    blood_pressure = st.text_input(
        "Blood Pressure",
        value="120/80",
        help="Enter blood pressure in the format 120/80."
    )

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# Prepare input data
# --------------------------------------------------

input_data = pd.DataFrame({
    "Gender": [gender],
    "Age": [age],
    "Occupation": [occupation],
    "Sleep Duration": [sleep_duration],
    "Physical Activity Level": [physical_activity],
    "Stress Level": [stress_level],
    "BMI Category": [bmi_category],
    "Blood Pressure": [blood_pressure],
    "Heart Rate": [heart_rate],
    "Daily Steps": [daily_steps]
})


# --------------------------------------------------
# Prediction section
# --------------------------------------------------

st.markdown(
    '<div class="section-heading">🔍 Generate Prediction</div>',
    unsafe_allow_html=True
)

predict_button = st.button("Predict My Sleep Quality")


if predict_button:

    # Validate blood pressure format
    blood_pressure_pattern = r"^\d{2,3}/\d{2,3}$"

    if not re.match(blood_pressure_pattern, blood_pressure):
        st.error(
            "Please enter blood pressure in the correct format, such as 120/80."
        )
        st.stop()

    systolic, diastolic = map(
        int,
        blood_pressure.split("/")
    )

    # Validate blood pressure ranges
    if not (70 <= systolic <= 250):
        st.error(
            "Systolic blood pressure must be between 70 and 250."
        )
        st.stop()

    if not (40 <= diastolic <= 150):
        st.error(
            "Diastolic blood pressure must be between 40 and 150."
        )
        st.stop()

    # Validate unusual values
    if sleep_duration < 4 or sleep_duration > 12:
        st.warning(
            "The entered sleep duration is unusual. Please verify the value."
        )

    if daily_steps > 30000:
        st.warning(
            "The entered daily steps value is unusually high. Please verify it."
        )

    if heart_rate < 50 or heart_rate > 120:
        st.warning(
            "The entered heart rate is outside the common resting range. "
            "Please verify the value."
        )

    if physical_activity > 150:
        st.warning(
            "The entered physical activity value is unusually high. "
            "Please verify it."
        )

    # Generate predictions internally
    prediction_one = model_one.predict(input_data)[0]
    prediction_two = model_two.predict(input_data)[0]

    # Final prediction
    final_prediction = prediction_two

    # Display result
    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-label">Your Predicted Sleep Quality</div>
            <div class="result-value">{final_prediction}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Suggestions
    if final_prediction == "Poor":
        suggestion = (
            "Your predicted sleep quality is Poor. Try maintaining a regular "
            "sleep schedule, reducing stress, limiting screen time before bed, "
            "and creating a comfortable sleeping environment."
        )

    elif final_prediction == "Average":
        suggestion = (
            "Your predicted sleep quality is Average. A consistent bedtime, "
            "sufficient sleep duration, regular physical activity, and balanced "
            "daily habits may help improve your sleep."
        )

    else:
        suggestion = (
            "Your predicted sleep quality is Good. Continue maintaining healthy "
            "sleep habits, regular physical activity, and a consistent routine."
        )

    st.markdown(
        f"""
        <div class="suggestion-card">
            <b>💡 General Suggestion</b><br><br>
            {suggestion}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="footer-note">
            This application is intended for educational purposes only.
            It is not medical advice or a medical diagnosis.
        </div>
        """,
        unsafe_allow_html=True
    )