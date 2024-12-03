import streamlit as st
from datetime import datetime

st.title("HAPPY 3 YEAR ANNIVERSARY")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFB6C1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'responses' not in st.session_state:
    st.session_state.responses = []

def save_response(response):
    st.session_state.responses.append(response)

def next_question(question, options=None, is_date=False):
    st.write(question)
    if is_date:
        date = st.date_input("Choose a date", datetime.today())
        if st.button("Next"):
            save_response(date)
            return True
    else:
        choice = st.selectbox("Select an option", options)
        if st.button("Next"):
            save_response(choice)
            return True
    return False

if next_question("What date are you available?", is_date=True):
    if next_question("Where would you love to go out and eat?", 
                     options=["Restaurant A", "Restaurant B", "Restaurant C", "Restaurant D"]):
        if next_question("Where do you want to get dessert?", 
                         options=["Ice Cream", "Boba", "Bread/Treats", "Dick"]):
            if next_question("Where would you like to spend the rest of the day?", 
                             options=["My House", "Open One of Your Christmas Gifts", "Take a Walk"]):
                st.markdown(
                    """
                    <h2 style='text-align: center;'>I LOVE YOU!</h2>
                    <h3 style='text-align: center;'>Thanks for helping me make your day better!</h3>
                    <div style='text-align: center;'>
                        <img src='https://example.com/flowers.png' width='300'/>
                    </div>
                    """,
                    unsafe_allow_html=True