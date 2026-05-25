import streamlit as st
import numpy as np
import joblib

from tensorflow.keras.models import load_model

# Load trained model
model = load_model("insurance_model.h5")

# Load scaler
scaler = joblib.load("scaler.pkl")

# App title
st.title("Medical Insurance Cost Prediction")

st.write("Enter patient information below")

# User inputs
age = st.number_input("Age", min_value=1, max_value=100)

sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0
)

children = st.number_input(
    "Children",
    min_value=0,
    max_value=10
)

smoker = st.selectbox(
    "Smoker",
    ["Yes", "No"]
)

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# Encoding
sex = 1 if sex == "Male" else 0

smoker = 1 if smoker == "Yes" else 0

region_mapping = {
    "northeast": 0,
    "northwest": 1,
    "southeast": 2,
    "southwest": 3
}

region = region_mapping[region]

# Prediction button
if st.button("Predict Insurance Cost"):

    input_data = np.array([
        [age, sex, bmi, children, smoker, region]
    ])

    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Insurance Cost: ${prediction[0][0]:.2f}"
    )