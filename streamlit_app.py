import streamlit as st
import datetime
# Title of the app
st.title("3 Year Anniversary Questionnaire")

# Initialize session state
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.answers = {}

# Questions list
questions = [
    "Do you love me? (Answer 'yes' or 'no')",
    "What's your favorite thing about me?",
    "What day are you available to hang out?",
    "Choose where you want to eat:",
    "Choose where you want to get dessert:",
]

# Function to display the current question
def display_question():
    if st.session_state.question_index < len(questions):
        question = questions[st.session_state.question_index]
        if question == questions[0]:
            answer = st.text_input(question)
            if answer.lower() == 'yes':
                st.session_state.answers[question] = answer
                st.session_state.question_index += 1
        elif question == questions[1]:
            answer = st.text_input(question)
            if answer:
                st.session_state.answers[question] = answer
                st.session_state.question_index += 1
        elif question == questions[2]:
            answer = st.date_input(question)
            st.session_state.answers[question] = answer
            st.session_state.question_index += 1
        elif question == questions[3]:
            answer = st.selectbox(question, ["Italian", "Chinese", "Mexican", "Indian"])
            st.session_state.answers[question] = answer
            st.session_state.question_index += 1
        elif question == questions[4]:
            answer = st.selectbox(question, ["Ice Cream", "Cake", "Cookies", "Brownies"])
            st.session_state.answers[question] = answer
            st.session_state.question_index += 1

# Display the current question
display_question()

# Final message
if st.session_state.question_index == len(questions):
    st.write("Appointment booked! Cya soon! 🌹❤️")
    st.write("Your answers:")
    for q, a in st.session_state.answers.items():
        st.write(f"{q}: {a}")