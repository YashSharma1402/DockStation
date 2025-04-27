# main.py
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Predictor")
st.markdown("Enter passenger information below:")

# Inputs
pclass = st.selectbox('Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
sex = st.selectbox('Sex', ['male', 'female'])
age = st.slider('Age', 0, 100, 25)
sibsp = st.slider('Siblings/Spouses Aboard', 0, 10, 0)
parch = st.slider('Parents/Children Aboard', 0, 10, 0)
fare = st.number_input('Passenger Fare', 0.0, 500.0, 32.0)

# Encode sex
sex_encoded = 1 if sex == 'male' else 0

# Predict
if st.button("Predict Survival"):
    input_features = np.array([[pclass, sex_encoded, age, sibsp, parch, fare]])
    prediction = model.predict(input_features)
    result = "Survived ✅" if prediction[0] == 1 else "Did Not Survive ❌"
    st.subheader(f"Prediction: {result}")
