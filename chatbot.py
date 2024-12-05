from nltk.chat.util import Chat, reflections
import streamlit as st

# Define the chatbot's data
data = [
    [r"(.*hi|.*hello|.*hey)", ["Hello"]],
    [r"(.*name)", ["My name is Oluwaseun"]],
    [r"(.*age|.*old)", ["I'm 23 years old"]],
    [r"(.*language)", ["I speak English and Yoruba"]],
    [r"(.*sports)", ["I like watching football and basketball"]],
    [r"(.*hobbies )", ["I like taking walks and listening to music"]],
    [r"(.*work)", ["Currently learning Data science"]],
    [r"(.*skills)", ["I'm average in Python, decent in SQL"]],
    [r"(.*expertise)", ["I would love to concentrate on machine learning"]],
    [r"(.*food)", ["My favorite food is anything meat"]],
    [r"(.*pets|.*pet)", ["I do not have any pets"]],
    [r"(.*goals)", ["My goal is to make models that solve world problems"]]
]

chatbot = Chat(data, reflections)

# Streamlit UI
st.title("Oluwaseun's Chatbot")
st.write("Type your question below, and I'll try to answer!")

# Input field
user_input = st.text_input("You:", "")

# Chatbot response
if user_input:
    if user_input.lower() == 'exit':
        st.write("Chatbot: Goodbye!")
    else:
        response = chatbot.respond(user_input)
        if response is None:
            st.write("Chatbot: I could not understand you, kindly rephrase your statement.")
        else:
            st.write("Chatbot:", response)
