import pickle
import streamlit as st 

with open('pickle file/model.pickle','rb') as file:
    model = pickle.load(file)

year = st.text_input('Years of Exprience')

if st.button('Submit'):
    y_pred = model.predict([[int(year)]])
    st.write(f'Your Salary must be around {y_pred[0]}')