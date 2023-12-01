import streamlit as st
from chat import get_response

st.title("Coffee shop Chatbot")
st.divider()
# temp = st.chat_message("assistant")
# temp.write(get_response("Hi"))

input = st.chat_input("")

# input = st.text_input(label="You :-")
count = 0


while True:
    if input:
        temp = st.chat_message("assistant")
        temp.write(get_response(input))
        # st.success(get_response(input))
        count = count + 1
        input = ""
        # input = st.text_input(label="You", key=count)


# count = 0
# input = st.chat_input(placeholder="You")
# while True:
#     if input != None:
#         temp = st.chat_message("assistant")
#         temp.write(get_response(input))
#         input = None
#         count = count + 1
#         input = st.chat_input(placeholder="You", key=count)
