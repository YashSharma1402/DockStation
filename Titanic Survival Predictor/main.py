import streamlit as st
import joblib
import pandas as pd

# Load Model
model = joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Prediction")

# User Input
pclass = st.selectbox("Passenger Class (1 = First, 2 = Second, 3 = Third)", [1, 2, 3])
sex = st.radio("Sex", ["Male", "Female"])
age = st.slider("Age", 0, 100, 30)
sibsp = st.slider("Number of Siblings/Spouses Aboard", 0, 10, 0)
parch = st.slider("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.slider("Fare Paid ($)", 0, 500, 50)
embarked = st.selectbox("Embarked Port", ["C", "Q", "S"])

# Convert Inputs to Numeric Values
sex = 1 if sex == "Male" else 0
embarked = {"C": 0, "Q": 1, "S": 2}[embarked]

# Prediction Button
if st.button("Predict Survival"):
    input_data = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare, embarked]],
                              columns=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"])
    prediction = model.predict(input_data)[0]
    st.success("🎉 Survived" if prediction == 1 else "❌ Did Not Survive")
