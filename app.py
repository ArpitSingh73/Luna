import streamlit as st
from chat import get_response


var = st.sidebar.radio("Navigation", ["Home", "About"])

if var == "Home":
    st.title("Coffee Shop Chatbot")
    st.divider()
    temp = st.chat_message("human")
    temp.write("Hi there, I am Luna. How can I help you?")
    input = st.chat_input("")

    while True:
        if input:
            temp = st.chat_message("assistant")
            temp.write(get_response(input))
            input = ""


elif var == "About":
    st.subheader(
        "Hi there, This is a simple Chatbot, developed for Coffee a Shop. I made this bot to implement my learning of Artificial Neural Networks(ANN). I used PyTorch as framework for model training & the data was manually created. It can answer questions about -"
    )

    st.text("Bot itself.")
    st.text("Service it offers.")
    st.text("Methods of payment.")
    st.text("Delivery info.")
