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

# Question 1: Date Availability
st.header("What date are you available?")
date = st.date_input("Choose a date", datetime.today())
if st.button("Next"):
    st.session_state.date = date

# Question 2: Where to eat
if 'date' in st.session_state:
    st.header("Where would you love to go out and eat?")
    choice = st.radio("Choose one:", ("Korean BBQ", "Pasta", "Steakhouse"))
    if choice == "Korean BBQ":
        st.balloons()
        st.image("https://example.com/smiley_face.png", width=200)
        if st.button("Next"):
    st.write("You clicked the Next button!")
        st.session_state.choice = choice

# Question 3: Dessert
if 'choice' in st.session_state:
    st.header("Where do you want to get dessert?")
    dessert_choice = st.radio("Choose one:", ("Ice Cream", "Boba", "Bread/Treats", "Dick"))
    if st.button("Next"):
        st.session_state.dessert_choice = dessert_choice

# Question 4: Spend the day
if 'dessert_choice' in st.session_state:
    st.header("Where would you like to spend the rest of the day?")
    day_choice = st.radio("Choose one:", ("My House", "Christmas in the Park", "Take a Walk"))
    if st.button("Next"):
        st.session_state.day_choice = day_choice

# Final Message
if 'day_choice' in st.session_state:
    st.header("I love you! Thanks for helping me make your day better!")
    st.markdown(
        """
        <style>
        .flowers {
            background-image: url('https://example.com/flowers_background.png');
            background-size: cover;
            height: 100vh;
        }
        </style>
        <div class="flowers"></div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()