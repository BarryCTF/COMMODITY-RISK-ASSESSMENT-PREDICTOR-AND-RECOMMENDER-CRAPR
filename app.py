import streamlit as st
from pycaret.classification import load_model
import plotly.express as px
import pandas as pd

# Initialise session state
if 'launch_screen' not in st.session_state:
    st.session_state.launch_screen = True

if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

if 'answers' not in st.session_state:
    st.session_state.answers = [None] * 12

# List of questions and options
questions = [
    "What is your primary investment goal?",
    "When do you plan to begin withdrawing money from your investments in?",
    "Which statement best describes your investment knowledge?",
    "How familiar are you with Commodities (Metals) and the risks and potential returns of such investments?",
    "What is your total gross annual household income?",
    "How much money have you set aside (outside of your pension / Central Provident Fund savings) in event of emergencies (e.g need to liquidate some of Portfolio due to Market volatility)?",
    "What is the maximum percentage of your portfolio you would allocate to a single investment?",
    "Inflation can reduce your spending power. How much risk are you willing to accept to counteract the effects of inflation?",
    "Choose the statement that best describes your attitude towards investing and inflation.",
    "Imagine six months after placing your investment, you discover that your portfolio value has decreased by 25%. What would you do?",
    """Say you possess $100,000 and wish to invest the funds for the future. 
    Which of these asset mixes would you choose to invest in?

    Investment A has an average return of 30% but the possibility of losing up to 40% in any year.
    Investment B has an average return of 3% with the possibility of losing up to 5% in any year.""",
    "In your opinion, what is the best strategy for growing your wealth?"
]

options_list = [
    ["Short-term needs (e.g., less than 3 years)", "Medium-term needs (e.g., 3-7 years)", "Long-term growth (e.g., more than 7 years)"],
    ["Less than 3 years", "3–5 years", "6–10 years", "11 years or more"],
    ["Novice. My knowledge of investing is limited.", "Good. I have a working knowledge of the major characteristics of the different types of investments and the financial marketplace.", "Excellent. I am a seasoned investor and have a comprehensive understanding of the different types of investments, their associated risks and how they relate to market volatility."],
    ["Not familiar", "Somewhat familiar", "Very familiar. I invest in stocks, bonds, options, etc."],
    ["Less than $30,000", "$30,000 - $59,999", "$60,000 - $99,999", "$100,000 - $199,999", "Over $200,000"],  
    ["Less than one month of living expenses", "Between one and six months of living expenses", "More than six months of living expenses"], 
    ["Less than 10%", "10% - 25%", "25% - 50%", "More than 50%"],
    ["Inflation may erode my savings over the long term, but am only willing to take limited risk to attempt to counter the effects of inflation", "I am conscious of the effects of inflation, and am prepared to take moderate risks in order to stay ahead of inflation", "I am comfortable with short to medium term losses in order to beat inflation over the longer term"],
    ["I want my investments to be safe and protected even if it means that my investments will not keep pace with inflation", "I am willing to accept a low level of fluctuation in the value of my investments in order to attempt to keep pace with inflation.", "I am willing to accept a moderate level of fluctuation in the value of my investments in order to attempt to achieve investment returns somewhat higher than inflation.", "I am willing to accept a high level of fluctuation in the value of my investments in order to attempt to significantly outperform the rate of inflation."],
    ["Close your entire position", "Consider reducing your position to preserve capital as you are uncomfortable with possible further losses in your portfolio.", "Would not take any action because it was a calculated risk and you expect future growth as you are comfortable with price volatility.", "Would consider investing more funds to lower your average position expecting future growth as you are comfortable with price volatility and you view such price reduction as buying opportunities."],
    ["Invest significantly more in B compared to A", "Invest equal amounts in both A and B", "Invest significantly more in A compared to B"],
    ["Avoiding risk to preserve capital.", "Taking some risk to achieve moderate growth.", "Taking significant risk to achieve high growth.", "Taking maximum risk to maximize potential returns."]
]


def calculate_points(responses):
    points = {}
    
    # q1
    if responses['q1'] == 1:
        points['q1-points'] = 1
    elif responses['q1'] == 2:
        points['q1-points'] = 3
    elif responses['q1'] == 3:
        points['q1-points'] = 5
    
    # q2
    if responses['q2'] == 1:
        points['q2-points'] = 1
    elif responses['q2'] == 2:
        points['q2-points'] = 3
    elif responses['q2'] == 3:
        points['q2-points'] = 5
    elif responses['q2'] == 4:
        points['q2-points'] = 7
    
    # q3
    if responses['q3'] == 1:
        points['q3-points'] = 1
    elif responses['q3'] == 2:
        points['q3-points'] = 3
    elif responses['q3'] == 3:
        points['q3-points'] = 5
    
    # q4
    if responses['q4'] == 1:
        points['q4-points'] = 1
    elif responses['q4'] == 2:
        points['q4-points'] = 3
    elif responses['q4'] == 3:
        points['q4-points'] = 5
    
    # q5
    if responses['q5'] == 1:
        points['q5-points'] = 1
    elif responses['q5'] == 2:
        points['q5-points'] = 2
    elif responses['q5'] == 3:
        points['q5-points'] = 3
    elif responses['q5'] == 4:
        points['q5-points'] = 4
    elif responses['q5'] == 5:
        points['q5-points'] = 5
    
    # q6
    if responses['q6'] == 1:
        points['q6-points'] = 1
    elif responses['q6'] == 2:
        points['q6-points'] = 3
    elif responses['q6'] == 3:
        points['q6-points'] = 5
    
    # q7
    if responses['q7'] == 1:
        points['q7-points'] = 1
    elif responses['q7'] == 2:
        points['q7-points'] = 3
    elif responses['q7'] == 3:
        points['q7-points'] = 5
    elif responses['q7'] == 4:
        points['q7-points'] = 7
    
    # q8
    if responses['q8'] == 1:
        points['q8-points'] = 1
    elif responses['q8'] == 2:
        points['q8-points'] = 3
    elif responses['q8'] == 3:
        points['q8-points'] = 5
    
    # q9
    if responses['q9'] == 1:
        points['q9-points'] = 0
    elif responses['q9'] == 2:
        points['q9-points'] = 1
    elif responses['q9'] == 3:
        points['q9-points'] = 3
    elif responses['q9'] == 4:
        points['q9-points'] = 5
    
    # q10
    if responses['q10'] == 1:
        points['q10-points'] = 0
    elif responses['q10'] == 2:
        points['q10-points'] = 1
    elif responses['q10'] == 3:
        points['q10-points'] = 3
    elif responses['q10'] == 4:
        points['q10-points'] = 5
    
    # q11
    if responses['q11'] == 1:
        points['q11-points'] = 1
    elif responses['q11'] == 2:
        points['q11-points'] = 3
    elif responses['q11'] == 3:
        points['q11-points'] = 5
    
    # q12
    if responses['q12'] == 1:
        points['q12-points'] = 0
    elif responses['q12'] == 2:
        points['q12-points'] = 1
    elif responses['q12'] == 3:
        points['q12-points'] = 3
    elif responses['q12'] == 4:
        points['q12-points'] = 5
    
    return points

# Function to handle navigation
def next_question():
    if st.session_state.question_index < len(questions) - 1:
        st.session_state.question_index += 1

def previous_question():
    if st.session_state.question_index > 0:
        st.session_state.question_index -= 1

# Welcome page
if st.session_state.question_index == 0 and st.session_state.launch_screen:
    st.title("Welcome to the Commodity Metals Portfolio Recommender")
    st.write("This Questionnaire will help us assess your Investor Risk profile before recommending your ideal portfolio.")
    if st.button("Start"):
        st.session_state.launch_screen = False

# Question pages
elif st.session_state.question_index <= 11:
    placeholder = st.empty()

    with placeholder.container():
        st.title(f"Question {st.session_state.question_index + 1}")
        st.write(questions[st.session_state.question_index])


        # Add a placeholder option as the first option to ensure no default selection
        options = options_list[st.session_state.question_index]


        # Check if there's already a selected answer for this question
        # If so, find the index of that answer in the options list
        if st.session_state.answers[st.session_state.question_index] is not None:
            selected_option = st.session_state.answers[st.session_state.question_index]
            index = options.index(selected_option)  # Get the index of the selected answer
        else:
            index = None  # If no answer has been selected, set index to None
            
        # Display the radio button and store the selection
        selected_option = st.radio(
            "Select an option:", 
            options, 
            index=index,  # This will not pre-select any option
            key=f"q{st.session_state.question_index}"  # Ensure a unique key for each question
        )
        
        #selected_option = st.radio(
         #  "Select an option:", 
          #  options_list[st.session_state.question_index], 
           #key=f"q{st.session_state.question_index}",
            #index=options_list[st.session_state.question_index].index(st.session_state.answers[st.session_state.question_index]) if st.session_state.answers[st.session_state.question_index] else 0
        #)

        # Store the selected option in session state
        st.session_state.answers[st.session_state.question_index] = selected_option

        col1, col2 = st.columns([1, 1])

        # Back button logic
        with col1:
            if st.session_state.question_index > 0:
                if st.button("Back"):  
                    previous_question()

        with col2:
            if st.session_state.question_index <= len(questions) - 2:
                if st.button("Next"):
                    # Only move to the next question if an option is selected
                    if selected_option is not None:
                        next_question()
                    else:
                        st.warning("Please select an option before proceeding.")
            elif st.session_state.question_index == len(questions) - 1:
                # Final question, display Finish button
                if st.button("Finish"):
                    # Move to the results page and rerun the app
                    st.session_state.question_index += 1  # Move to the result page
                    
        
        #with col2:
        #    if st.session_state.question_index <= len(questions) - 2:
        #        if st.button("Next"):
        #            next_question()
        #    elif st.session_state.question_index == len(questions) - 1:
        #        if st.button("Finish"):
        #            st.session_state.question_index +=1

# Once final question has been answered                    
elif st.session_state.question_index == 12:
     
    placeholder = st.empty()
    
    with placeholder.container():
        
        st.header("Your Results")

        # Collect user responses
        user_responses = {}
        
        for i, answer in enumerate(st.session_state.answers, 1):
            if i <= 12:
                
                # Store the question number and option number selected by the user
                user_responses[f"q{i}"] = options_list[i-1].index(answer)+1
                

        # Calculate the points based on user choices for the 12 questions
        #points = calculate_points(user_responses)

        # Check if calculate_points is defined and works correctly
        try:
            points = calculate_points(user_responses)
        except Exception as e:
            st.error(f"Error calculating points: {e}")
            points = {}  # Handle cases where points calculation fails
        
        # Combine responses and points into one dictionary
        # This syntax unpacks both dictionaries into a new dictionary.
        combined_dict = {**user_responses, **points}

        # Create a Data Frame from the combined dictionary
        user_input_df = pd.DataFrame([combined_dict])
        
        # Make Predictions
        #model = load_model("model")
        #prediction = model.predict(user_input_df)[0]
        #st.write("Prediction is ", prediction)        



        # Load and make predictions using the model
        try:
            model = load_model("model")
            prediction = model.predict(user_input_df)[0]
            st.write("Risk Portrait is: ", prediction)  
        except Exception as e:
            st.error(f"Error loading model or making prediction: {e}")
            prediction = None  # Handle failure in model loading or prediction
        
        if prediction:

            # Calculate and display the total points after "Risk Portrait"
            total_points = sum(points.values())
            st.write(f"Total Points: {total_points}")
            
            # Define the data labels for the pie chart
            labels = ['Gold', 'Silver', 'Copper']
        
            # Determine portfolio breakdown depending on model prediction on user input
            if prediction == "Conservative":
                values = [70, 20, 10]
            elif prediction == "Moderately Conservative":
                values = [40, 45, 15]
            elif prediction == "Moderate":
                values = [25, 50, 25]
            elif prediction == "Moderately Aggressive":
                values = [20, 35, 45]
            elif prediction == "Aggressive":
                values = [10, 20, 70]
            else:
                values = [0, 0, 0]  # Handle unexpected predictions
            
            portfolio_df = pd.DataFrame({
                'Metal': labels,
                'Percentage': values
            })

            # Define the colors for each metal
            color_map = {'Gold': 'gold', 'Silver': 'silver', 'Copper': 'darkorange'}
        
            # Create the pie chart
            fig = px.pie(portfolio_df, values='Percentage', names='Metal', title="Your Ideal Portfolio", color='Metal', color_discrete_map=color_map)
            st.plotly_chart(fig, theme=None)

        else:
            st.error("Could not generate the portfolio breakdown due to missing prediction.")

        st.write("Here are the choices you made:")
        
        for i, answer in enumerate(st.session_state.answers, 1):
            if i <= 12:
                
                st.write(f"**Question {i}:** {questions[i-1]}")
                st.write(f"**Your choice:** {options_list[i-1].index(answer)+1}")
                st.write(f"**Your answer:** {answer}")
                st.write("---")        
        
        

        if st.button("Restart"):
            st.session_state.launch_screen = True
            st.session_state.question_index = 0
            st.session_state.answers = [None] * 12
            st.experimental_rerun()