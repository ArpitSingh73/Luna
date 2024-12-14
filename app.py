import streamlit as st
from chat import get_response


var = st.sidebar.radio("Navigation", ["Home", "About"])

if var == "Home":
    st.title("Coffee Shop Chatbot")
    st.divider()
    temp = st.chat_message("human")
    temp.write("Hi there, I am Luna. How can I help you?")
    input = st.chat_input("")

    # while True:
    #     if input:
    #         temp = st.chat_message("assistant")
    #         temp.write(get_response(input))
    #         input = ""

   
    if input:
        while input:    
            temp = st.chat_message("assistant")
            temp.write(get_response(input))
            input = ""

elif var == "About":
    st.subheader(
        "Hi there, This is a simple Chatbot, developed for a Coffee Shop. I made this bot to implement my learnings of Artificial Neural Networks(ANN). It's a simple food forward neural Network with 2 hidden layes and 8 nodes each, ReLU acts as activation function and finally Cross-entrpy loss in output. I used PyTorch as framework for model training & the data was manually created. It can answer questions about -"
    )

    st.text("Bot itself.")
    st.text("Prices' information.")
    st.text("Methods of payment.")
    st.text("Product comparison.")
    st.text("Service it offers.")
    st.text("Delivery info.")
