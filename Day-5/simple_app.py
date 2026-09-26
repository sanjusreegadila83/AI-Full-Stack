import streamlit as st
st.title("My first Streamlit App!!!")
st.subheader("About simple_app")
st.header("Welcome to my AI application!")
name = st.text_input("Enter your Name: ")
if st.button("submit"):
    st.write("Hello", name)
    st.markdown("Hello")
    