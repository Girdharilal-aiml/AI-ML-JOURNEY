import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.big-title {
    text-align: center;
    color: #ff4b4b;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 30px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    '<div class="big-title">❤️ Heart Disease Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Powered Health Risk Assessment</div>',
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.header("Patient Information")

age = st.sidebar.slider("Age", 18, 100, 40)

sex = st.sidebar.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.sidebar.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "TA", "ASY"]
)

resting_bp = st.sidebar.number_input(
    "Resting Blood Pressure",
    80, 200, 120
)

cholesterol = st.sidebar.number_input(
    "Cholesterol",
    100, 600, 200
)

fasting_bs = st.sidebar.selectbox(
    "Fasting Blood Sugar >120",
    [0, 1]
)

resting_ecg = st.sidebar.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.sidebar.slider(
    "Maximum Heart Rate",
    60, 220, 150
)

exercise_angina = st.sidebar.selectbox(
    "Exercise Angina",
    ["Y", "N"]
)

oldpeak = st.sidebar.slider(
    "Oldpeak",
    0.0, 6.0, 1.0
)

st_slope = st.sidebar.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

# ---------------- DASHBOARD ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Age", age)

with col2:
    st.metric("Cholesterol", cholesterol)

with col3:
    st.metric("Max HR", max_hr)

st.divider()

# ---------------- PREDICT ----------------
if st.button("🔍 Predict Risk", use_container_width=True):

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    st.divider()

    if prediction == 1:
        st.error(
            "⚠️ High Risk of Heart Disease\n\nPlease consult a healthcare professional."
        )

    else:
        st.success(
            "✅ Low Risk of Heart Disease\n\nMaintain a healthy lifestyle."
        )

    # Probability (if model supports it)
    try:
        probability = model.predict_proba(scaled_input)[0]

        st.subheader("Risk Score")

        st.progress(float(probability[1]))

        st.write(
            f"**Heart Disease Probability:** "
            f"{probability[1]*100:.2f}%"
        )

    except:
        pass