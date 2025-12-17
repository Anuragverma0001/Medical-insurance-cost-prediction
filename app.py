`import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Medical Insurance Cost Prediction")

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Medical Insurance Cost Prediction")
st.write("Enter the details below to predict insurance cost.")

age = st.slider("Age", 18, 100, 25)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
children = st.number_input("Number of Children", 0, 10, 0)

sex = st.selectbox("Sex", ["Female", "Male"])
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox(
    "Region",
    ["Northeast", "Northwest", "Southeast", "Southwest"]
)

# Encoding (must match training)
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0

region_map = {
    "Northeast": 0,
    "Northwest": 1,
    "Southeast": 2,
    "Southwest": 3
}
region = region_map[region]

if st.button("Predict Insurance Cost"):
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ₹ {prediction[0]:.2f}")
`
