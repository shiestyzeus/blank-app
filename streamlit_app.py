# HAPPY 3 YEAR ANNIVERSARY

import streamlit as st

st.title("Happy 3 Year Anniversary ❤️")

# Question 1
answer1 = st.text_input("What is your favorite memory with me?")
if answer1:
    # Question 2
    answer2 = st.text_input("What do you love most about our relationship?")
    if answer2:
        # Question 3
        answer3 = st.text_input("What are you looking forward to in our future together?")
        if answer3:
            st.success("Thank you for sharing your thoughts! I love you!")