import streamlit as st
import pandas as pd
from datetime import datetime
import calendar

# Initialize session state to store answers
if 'answers' not in st.session_state:
    st.session_state.answers = []

# Function to display questions
def display_question(question, input_type='text', options=None):
    st.write(question)
    if input_type == 'text':
        answer = st.text_input("Your answer:")
    elif input_type == 'date':
        answer = st.date_input("Choose a date:", datetime.now())
    elif input_type == 'select':
        answer = st.selectbox("Choose an option:", options)
    else:
        answer = None

    if st.button("Next"):
        if answer:
            st.session_state.answers.append(answer)
            return True
    return False

# Question 1
if display_question("Do you love me?", input_type='text'):
    # Question 2
    if display_question("What's your favorite thing about me?"):
        # Question 3
        if display_question("What day are you available to hang out?", input_type='date'):
            # Question 4
            if display_question("Choose where you wanna eat:", input_type='select', options=["KBBQ", "Steakhouse", "Other"]):
                # Question 5
                if display_question("Choose where you want to get dessert:", input_type='select', options=["Ice Cream Shop", "Bakery", "Other"]):
                    # Final message
                    st.write("Appointment booked! Cya soon! 🌸❤️")
                    st.write("Your answers:")
                    st.write(st.session_state.answers)
                    st.balloons()