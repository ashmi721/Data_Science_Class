import streamlit as st 
import pickle

with open('model1.pickle','rb') as file:
    model1 = pickle.load(file)
    
year = st.text_input(" Years of Exprience ")
education_labels = {'Bachelor':0, 'Master':1, 'PhD':2}    
education = st.selectbox('Education Level',('Bachelor','Master','PhD'))

if st.button('Calculate'):
  education_levels = education_labels.get(education,0)
  y_pred = model1.predict([[int(year),education_levels]])
  st.write(f"Your Salary must be around {y_pred[0]} in {year} Years Exprience, with  {education} Education Level")
  
   