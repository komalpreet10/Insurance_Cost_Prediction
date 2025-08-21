import streamlit as st
import pickle
import numpy as np

# Load the model
with open('training/models/model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Health Insurance Premium Predictor")

# Input fields
age = st.number_input("Age", min_value=0)
diabetes = st.selectbox("Diabetes (0 = No, 1 = Yes)", [0, 1])
bp_problems = st.selectbox("Blood Pressure Problems (0 = No, 1 = Yes)", [0, 1])
transplants = st.selectbox("Any Transplants (0 = No, 1 = Yes)", [0, 1])
chronic_diseases = st.selectbox("Any Chronic Diseases (0 = No, 1 = Yes)", [0, 1])
height = st.number_input("Height (cm)", min_value=0.0)
weight = st.number_input("Weight (kg)", min_value=0.0)
allergies = st.selectbox("Known Allergies (0 = No, 1 = Yes)", [0, 1])
cancer_history = st.selectbox("History of Cancer in Family (0 = No, 1 = Yes)", [0, 1])
major_surgeries = st.selectbox("Number of Major Surgeries", [0, 1, 2, 3])



# Calculate BMI
height_m = height / 100
bmi = weight / (height_m ** 2) if height_m > 0 else 0
st.write(f"Calculated BMI: {bmi:.2f}")


# One-hot encode NumberOfMajorSurgeries manually
surgery_1 = 1 if major_surgeries == 1 else 0
surgery_2 = 1 if major_surgeries == 2 else 0
surgery_3 = 1 if major_surgeries == 3 else 0

# Prepare input data


input_data = np.array([[
    age,
    diabetes,
    bp_problems,
    transplants,
    chronic_diseases,
    height,
    weight,
    allergies,
    cancer_history,
    bmi,
    surgery_1,
    surgery_2,
    surgery_3
]])


# Predict
if st.button("Predict Premium Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Premium Price: ${prediction[0]:.2f}")
