import pickle
import streamlit as st

with open('Spam_classifire.pickle','rb') as file:
    model = pickle.load(file) 
    
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    email : str

app = FastAPI()

@app.get("/")
def home_page():
    return {"Msg":'Spam classifire model is running'}

@app.post("/classify")
def classify(item:Data):
    y_pred = model.predict({item.email})
    return {'label':y_pred[0]}