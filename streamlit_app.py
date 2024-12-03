import streamlit as st
from datetime import datetime
import requests

# Function to display the GIF
def display_gif(gif_url):
    st.image(gif_url, use_column_width=True)

# Page 1: Availability Question
st.title("3 Year Anniversary Questionnaire")
st.header("Question #1")
st.write("Are you available on...")

# Calendar for date selection
date = st.date_input("Select a date:", datetime.now())

# Display the GIF in the middle
gif_url_1 = "https://media.tenor.com/images/1c1e1c1e1c1e1c1e1c1e1c1e1c1e1c1e/tenor.gif"
display_gif(gif_url_1)

# Next button to proceed to the next question
if st.button("Next"):
    st.session_state.page = 2

# Page 2: Thank You Message
if 'page' in st.session_state and st.session_state.page == 2:
    st.header("Thank You!")
    gif_url_2 = "https://media.tenor.com/images/2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d/tenor.gif"
    display_gif(gif_url_2)
    
    if st.button("Next"):
        st.write("Looking forward to our special day!")