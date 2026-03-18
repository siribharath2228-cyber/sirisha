import streamlit as st

# Title
st.title("My First Streamlit App")

# Text
st.write("Hello, welcome to Streamlit!")

# User input
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! 👋")

# Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write("Your age is:", age)

# Button
if st.button("Click Me"):
    st.success("Button clicked!")