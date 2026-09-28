import ollama
import streamlit as st
st.header(":rainbow[🤖 Welcome to my chatBot!!!]")
with st.sidebar:
        st.subheader(":orange[Chat Settings]")
        if st.badge("Clear Chat",color="yellow"):
            st.session_state.messages=[]
        personalities = {
            "Kid" : "Answer the questions like you are explaining to a 5 years old kid.Give the answer in 2 lines only.",
            "Friend" : "Answer the questions in a friendly and casula manner.Give the answer in 2 lines.",
            "IT Employee" : "Answer the questions like you are giving suggestions to a fresher.Give the answer in 2 lines."
        }
        personality = st.selectbox("Select a personality",personalities.keys())      
        uploaded_file = st.file_uploader("upload a text file...")
        try:
            if uploaded_file:
                content = uploaded_file.read().decode("utf-8")
                st.badge("👍 successfully", color="blue")
                if st.button(":green[Display]"):
                    st.text(content)
        except:
            st.error("File not supported")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("Enter the question: ")
if question:
    st.session_state.messages.append(
            { "role": "user",
            "content": question}
        )
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Loading...."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {"role" : "system" , "content": personalities[personality]}]
                + st.session_state.messages)
        st.session_state.messages.append(
            {"role": "assistant",
             "content": response["message"]["content"]}
            )
    with st.chat_message("assistant"):
        st.write("AI:", response["message"]["content"])


