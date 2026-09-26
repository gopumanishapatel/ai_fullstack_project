import ollama
import streamlit as st
st.title("welcome to my ChatBot app!!!")
with st.sidebar:
    uploaded_file = st.file_uploader("upload a text file...")
    if uploaded_file:
        st.write("file is successfully uploaded")
        context = uploaded_file.read().decode("utf-8")
        st.text(context)
if "messages" not in st.session_state:
     st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
    with st.spinner("loading..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=st.session_state.messages
)
question = st.chat_input("You:")
if question:
    st.session_state.messages.append(
    {
        "role":"user",
        "content":question
    }
)
with st.chat_message("user"):
    st.write(question)
response = ollama.chat(
    model="llama3.2:3b",
    messages=st.session_state.messages
)
st.session_state.messages.append(
    {
        "role":"assistant",
        "content": response["message"]["content"]
    }    
)
with st.chat_message('assistant'):
    st.write(response["message"]["content"])


   