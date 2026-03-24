import streamlit as st

st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = num1**2
st.write(f"The square of {num1} is {num2}")

num3 = num1**3
st.write(f"The cube of {num1} is {num3}")