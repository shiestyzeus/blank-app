import streamlit as st
import datetime

# Title
st.title("HAPPY 3 YEAR ANNIVERSARY ❤️")

# Start Button
if st.button("CLICK START TO BEGIN"):
    # First Question
    date = st.date_input("What day are you available?", datetime.date.today())
    
    # Second Question
    food_choice = st.selectbox("Where would you want to go eat?", 
                                ["KOREAN BBQ", "PASTA", "STEAKHOUSE"])
    
    # Third Question
    dessert_choice = st.selectbox("Where do you want to get for dessert?", 
                                   ["ICE CREAM", "BOBA", "DICK"])
    
    # Final Question
    activity_choice = st.selectbox("Where do you want to go once we finish?", 
                                    ["CHRISTMAS IN THE PARK", "IN MY ROOM CUDDLED UP"])
    
    # Thank You Message
    st.write("Thank you for helping me plan our special day! ❤️🌸")
    st.balloons()