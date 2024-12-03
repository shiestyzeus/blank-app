import streamlit as st
from datetime import datetime

# Set the page title and background color
st.title("Happy 3 Year Anniversary")
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #ff7f7f, #ffb3b3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Question 1: Date selection
st.header("What date are you available?")
date = st.date_input("Choose a date", datetime.today())
if st.button("Next"):
    st.session_state.date = date

# Question 2: Dining preference
if 'date' in st.session_state:
    st.header("Where would you love to go out to eat?")
    dining_choice = st.selectbox("Choose one", ["Korean BBQ", "Pasta", "Steakhouse"])
    if st.button("Next"):
        st.session_state.dining_choice = dining_choice

# Question 3: Dessert preference
if 'dining_choice' in st.session_state:
    st.header("Where do you want to get dessert?")
    dessert_choice = st.selectbox("Choose one", ["Ice Cream", "Boba", "Bread/Treats", "Dick"])
    if st.button("Next"):
        st.session_state.dessert_choice = dessert_choice

# Question 4: Day preference
if 'dessert_choice' in st.session_state:
    st.header("Where would you like to spend the rest of the day?")
    day_choice = st.selectbox("Choose one", ["My House", "Christmas in the Park", "Take a Walk"])
    if st.button("Finish"):
        st.session_state.day_choice = day_choice
        st.balloons()
        st.markdown("I love you! Thanks for helping me make your day better! 🌸❤️")