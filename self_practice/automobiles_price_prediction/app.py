import pickle
import streamlit as st

with open('automobiles_price_prediction\Automobilesmodel.pkl','rb') as file:
    model = pickle.load(file) 
    
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
   pass

app = FastAPI()

@app.get("/")
def home_page():
   pass

@app.post("/classify")
def classify():
    pass
   