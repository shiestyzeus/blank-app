import streamlit as st

st.title("A Special Test for My Girlfriend")
st.header("Welcome to Your Special Test!")
st.write("Let's see how well you know me.")
questions = {
    "What is my favorite color?": ["Red", "Blue", "Green", "Yellow"],
    "What is my favorite food?": ["Pizza", "Sushi", "Burger", "Pasta"],
    "Where did we first meet?": ["School", "Park", "Cafe", "Library"],
    "What is my favorite movie?": ["Inception", "Titanic", "Avatar", "The Matrix"],
}

score = 0

for question, options in questions.items():
    answer = st.radio(question, options)
    if answer == options[0]:  # Assuming the first option is the correct answer
        score += 1

if st.button("Submit"):
    st.write(f"Your score is: {score}/{len(questions)}")
    if score == len(questions):
        st.success("Perfect score! You really know me well!")
    else:
        st.warning("Good try! But there's always room for improvement.")

st.sidebar.header("About Us")
st.sidebar.write("This test is a fun way to celebrate our relationship!")
