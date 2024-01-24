import streamlit as st
import pickle

with open('spam_classifire.pkl', 'rb') as file:
    tfidf = pickle.load(file)


st.title('Email/SMs Spam Classifier')
input_sms = st.text_input("Enter the message:")

if st.button('Predict'):

    result = tfidf.predict([input_sms])

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

