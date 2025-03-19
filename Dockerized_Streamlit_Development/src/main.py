import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚀 Streamlit Dockerized App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    fig = px.histogram(df, x=df.columns[0])
    st.plotly_chart(fig)
