import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
ps = PorterStemmer()


def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  y= []
  for i in text:
    if i.isalnum():
      y.append(i)

  
  text = y[:] 
  y.clear() 

  for i in text:
    if i not in nltk.corpus.stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

with open('vectorizer.pkl','rb') as file:
    tfidf = pickle.load(file)
    
model = pickle.load(open('model.pkl','rb'))

st.title('Email/SMs Spam Classifier')
input_sms = st.text_input("Enter the message:")

if st.button('Predict'):
# preprocess
    transformd_sms = transform_text(input_sms)
   
    vector_input = tfidf.transform([transformd_sms])
    result = model.predict(vector_input)[0]
    
    if result == 1:
          st.header("Spam")
    else:    
          st.header("Not Spam")
    