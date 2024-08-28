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


## Question 1

# Title for the slide
st.title("Time Horizon")

# Display the question
st.subheader("Question 1: What is your primary investment goal?")

# Provide options for the question
options = [
    "Short-term needs (e.g., less than 3 years)",
    "Medium-term needs (e.g., 3-7 years)",
    "Long-term growth (e.g., more than 7 years)"
]

# Radio button to select an option
selected_option = st.radio("Select an option:", options)

# Display the selected option
#st.write(f"You selected: {selected_option}")

# Navigation buttons
if st.button("NEXT", key='next1'):
    st.write("Proceeding to the next question...")
    



## Question 2

# Title for the slide
st.title("Time Horizon")

# Display the question
st.subheader("Question 2: When do you plan to begin withdrawing money from your investments in?")

# Provide options for the question
options = [
    "Less than 3 years",
    "3–5 years",
    "6–10 years"
    "11 years or more"
]

# Radio button to select an option
selected_option = st.radio("Select an option:", options)

# Display the selected option
#st.write(f"You selected: {selected_option}")

# Navigation buttons
if st.button("NEXT", key='next2'):
    st.write("Proceeding to the next question...")
    
if st.button("BACK", key='back2'):
    st.write("Returning to the previous question...")


## Question 12

# Title for the slide
st.title("Risk Tolerance")

# Display the question
st.subheader("Question 12: In your opinion, what is the best strategy for growing your wealth?")

# Provide options for the question
options = [
    "Avoiding risk to preserve capital",
    "Taking some risk to achieve moderate growth",
    "Taking significant risk to achieve high growth"
    "Taking maximum risk to maximize potential returns"
]

# Radio button to select an option
selected_option = st.radio("Select an option:", options)

# Display the selected option
#st.write(f"You selected: {selected_option}")

# Navigation buttons
    
if st.button("BACK", key='back12'):
    st.write("Returning to the previous question...")

# Display the "FINISH" button after the last question

if st.button("FINISH", key='finish'):
    st.write("Questionnaire done. Do you wish to proceed?")
    
     # Display "Yes" and "No" buttons after clicking "FINISH"
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes", key='yes'):
            st.write("You chose to proceed. Proceeding with the next steps...")

    with col2:
        if st.button("No", key='no'):
            st.write("Go back")
