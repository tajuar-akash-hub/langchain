from langchain_groq import ChatGroq
from dotenv import load_dotenv 
import streamlit as st

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

st.header("Chatbot")

#chatbot 

user_input = st.chat_input("Type your message")

if user_input:
    if user_input.strip().lower() == 'exit':
        st.stop()

    with st.chat_message("user"):
        st.write(user_input)

    result = model.invoke(user_input)


    with st.chat_message('assistant'):
        st.write(result.content)


