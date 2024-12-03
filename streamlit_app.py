import streamlit as st
import pandas as pd
from datetime import datetime
# Initialize session state to store answers
if 'answers' not in st.session_state:
    st.session_state.answers = []

# Function to display questions
def display_question(question, options=None, input_type='text'):
    st.write(question)
    if input_type == 'text':
        answer = st.text_input("Your answer:")
    elif input_type == 'date':
        answer = st.date_input("Choose a date:", datetime.today())
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
    st.session_state.current_question = 2

# Question 2
if st.session_state.get('current_question', 1) == 2:
    if display_question("What's your favorite thing about me?"):
        st.session_state.current_question = 3

# Question 3
if st.session_state.get('current_question', 1) == 3:
    if display_question("What day are you available to hang out?", input_type='date'):
        st.session_state.current_question = 4

# Question 4
if st.session_state.get('current_question', 1) == 4:
    if display_question("Choose where you wanna eat:", options=["KBBQ", "Steakhouse", "Other"], input_type='select'):
        st.session_state.current_question = 5

# Question 5
if st.session_state.get('current_question', 1) == 5:
    dessert_places = ["Ice Cream Shop", "Bakery", "Chocolate Factory"]
    if display_question("Choose where you want to get dessert:", options=dessert_places, input_type='select'):
        st.session_state.current_question = 6

# Final Message
if st.session_state.get('current_question', 1) == 6:
    st.write("Appointment booked! Cya soon! 🌹❤️")
    st.balloons()
    st.write("Your answers:")
    st.write(st.session_state.answers)