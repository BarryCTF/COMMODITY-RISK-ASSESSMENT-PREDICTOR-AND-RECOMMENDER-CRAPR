import streamlit as st
import pandas as pd
import numpy as np



st.title("Capstone Project: Metal Recommender")


risk_data = pd.read_csv("data-risk-portrait.csv")
st.write(risk_data.head(100))
st.text("This Model is to determine Investor's Risk profile and suitable Metal Portfolio")

