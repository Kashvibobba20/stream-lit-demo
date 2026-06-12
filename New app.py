import streamlit as st

st.title("Welcome App")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}! 👋")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"Selected age: {age}")

if st.button("Celebrate"):
    st.balloons()

 st.title("Hello World App")
st.write("Hello, World!")

streamlit run app.py
   