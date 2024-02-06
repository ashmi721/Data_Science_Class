import pickle
import streamlit as st
import pandas as pd

df = pd.read_csv('Cleaned_car.csv')

with open('Automobilesmodel.pkl','rb') as file:
    model = pickle.load(file) 
    
    
def filter_data(category):
    return df[df['Category'] == category]
  
st.title('Automobiles price prediction')
Category = st.selectbox('Select Category',(df['Category'].unique()))
# Filter data based on the selected category
filtered_data = filter_data(Category)

Manufacturer = st.selectbox('Select Manufacturers',(filtered_data['Manufacturer'].unique()))    
Model = st.selectbox('Model',(filtered_data['Model'].unique()))
Year = st.selectbox('Est Year',(filtered_data['Prod. year'].unique()))

Leather_interior = st.selectbox('Select Leather interior',(filtered_data['Leather interior'].unique()))
Engine_volume = st.selectbox('Select Engine volume',(filtered_data['Engine volume'].unique()))
levy = st.selectbox('Select Levy',(filtered_data['Levy'].unique()))
kms = st.selectbox('Kms driven',(filtered_data['Mileage'].unique()))
Fuel  = st.selectbox('Fuel type',(filtered_data['Fuel type'].unique()))


if st.button('Predict'):
   user_features = pd.DataFrame({
        'Category name': [Category],
        'Manufacturer name': [Manufacturer],
        'Model type': [Model],
        'Prod. year': [Year],
        'leather seats': [Leather_interior],
        'Engine volume': [Engine_volume],
        'Mileage': [int(kms)],
        'Levy':[float(levy)],
        'Fule_type': [Fuel],
        
    })
   predicted_price = model.predict(user_features)[0] 
   st.write(f'Predicted Price: ${predicted_price:.2f}')
   