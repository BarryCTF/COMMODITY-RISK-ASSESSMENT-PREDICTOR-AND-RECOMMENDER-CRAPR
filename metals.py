import streamlit as st
import pandas as pd
import numpy as np



# Title of the project
st.title("CAPSTONE PROJECT PHASE I")

# Welcome message
st.header("WELCOME TO COMMODITIES METALS PORTFOLIO RECOMMENDER")


# Action button
if st.button("CLICK HERE TO PROCEED"):
    st.write("Bringing you to next page.")


# Prototype disclaimer on bottom right of page
st.markdown(
    """
    <style>
    .bottom-right {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-weight: bold;
    }
    </style>
    <div class="bottom-right">**This is still a prototype. Subject to changes**</div>
    """,
    unsafe_allow_html=True
)



risk_data = pd.read_csv("data-risk-portrait.csv")
st.write(risk_data.head(100))
