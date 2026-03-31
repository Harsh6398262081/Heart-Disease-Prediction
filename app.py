import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("❤️ Heart Disease Prediction")
st.markdown("### Enter Patient Details")

# ---------------- INPUTS ---------------- #

age = st.slider("Age", 20, 80, 40)

gender = st.selectbox("Gender", ["Male", "Female"])
isfemale = 1 if gender == "Female" else 0

resting_bp = st.slider("Resting Blood Pressure", 80, 200, 120)

cholesterol = st.slider("Cholesterol", 100, 600, 200)

fasting_bs = st.selectbox("Fasting Blood Sugar > 120", ["No", "Yes"])
fasting_bs = 1 if fasting_bs == "Yes" else 0

max_hr = st.slider("Max Heart Rate", 60, 220, 150)

exercise_angina = st.selectbox("Exercise Angina", ["No", "Yes"])
exercise_angina = 1 if exercise_angina == "Yes" else 0

oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)

# ---------------- ONE HOT ENCODING ---------------- #

# Chest Pain Type
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
cp_ata = 1 if chest_pain == "ATA" else 0
cp_nap = 1 if chest_pain == "NAP" else 0
cp_ta = 1 if chest_pain == "TA" else 0

# Resting ECG
rest_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
ecg_normal = 1 if rest_ecg == "Normal" else 0
ecg_st = 1 if rest_ecg == "ST" else 0

# ST Slope
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])
slope_flat = 1 if st_slope == "Flat" else 0
slope_up = 1 if st_slope == "Up" else 0

# ---------------- PREDICTION ---------------- #

if st.button("Predict"):

    # Arrange data EXACTLY like training
    input_data = np.array([[ 
        age, isfemale, resting_bp, cholesterol, fasting_bs,
        max_hr, exercise_angina, oldpeak,
        cp_ata, cp_nap, cp_ta,
        ecg_normal, ecg_st,
        slope_flat, slope_up
    ]])

    # Scale numeric columns ONLY
    scale_cols_index = [0, 2, 3, 5, 7]
    input_data[:, scale_cols_index] = scaler.transform(input_data[:, scale_cols_index])

    # Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # ---------------- OUTPUT ---------------- #

    st.markdown("## Result")

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease ({probability*100:.2f}%)")
    else:
        st.success(f"✅ Low Risk of Heart Disease ({probability*100:.2f}%)")

    # Progress bar
    st.progress(int(probability * 100))

st.markdown("---")
st.caption("Built by Harsh Kumar 🚀")