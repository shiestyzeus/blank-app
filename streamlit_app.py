import streamlit as st
import datetime

# Title
st.title("HAPPY 3 YEAR ANNIVERSARY ❤️")

# Start button
if st.button("START"):
    # First question
    date = st.date_input("What day are you available?", datetime.date.today())
    
    # Second question
    food_choice = st.selectbox("Where would you want to go eat?", 
                                ["KOREAN BBQ", "PASTA", "STEAKHOUSE"])
    
    # Third question
    dessert_choice = st.selectbox("Where do you want to get for dessert?", 
                                   ["ICE CREAM", "BOBA", "DICK"])
    
    # Final question
    activity_choice = st.selectbox("Where do you want to go once we finish?", 
                                    ["CHRISTMAS IN THE PARK", "IN MY ROOM CUDDLED UP"])
    
    # Thank you message
    st.markdown("Thank you for helping me plan our special day! ❤️🌸")
    st.balloons()