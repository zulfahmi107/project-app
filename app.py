import streamlit as st
st.title("My first Streamlit App")
st.write("Welcome to Streamlit!")
name = st.text_input("enter your name")

if st.button("submit"):
    st.success(f"Hello {name}")