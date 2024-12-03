import streamlit as st
from datetime import datetime

# Title
st.title("HAPPY 3 YEAR ANNIVERSARY")

# Question 1: Date Picker
st.header("What date are you available?")
date = st.date_input("Choose a date", datetime.today())

if st.button("Next"):
    # Question 2: Restaurant Choices
    st.header("Where would you love to go out and eat?")
    restaurants = ["Restaurant A", "Restaurant B", "Restaurant C", "Restaurant D"]
    choice = st.selectbox("Select a restaurant", restaurants)

    if st.button("Next"):
        # Question 3: Dessert Choices
        st.header("Where do you want to get dessert?")
        dessert_choices = ["Ice Cream", "Boba", "Bread/Treats", "Dick"]
        dessert = st.selectbox("Select a dessert", dessert_choices)

        if st.button("Next"):
            # Question 4: Spend the Day
            st.header("Where would you like to spend the rest of the day?")
            day_choices = ["My House", "Open one of your Christmas gifts", "Take a walk"]
            day_choice = st.selectbox("Select an option", day_choices)

            if st.button("Finish"):
                # Thank You Message
                st.header("I LOVE YOU!")
                st.write("Thanks for helping me make your day better!")
                st.markdown("<h1 style='text-align: center; color: pink;'>🌸🌸🌸</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: center; color: red;'>❤️❤️❤️</h1>", unsafe_allow_html=True)