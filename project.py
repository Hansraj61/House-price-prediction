import streamlit as st
import pandas as pd 
import numpy as np
import os
import pickle

st.image(r"innomatics.jpg", width=200)

st.title("HOUSE PRICE PREDICTION")

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(script_dir, "lr.pkl")

# Load the model
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    st.write("Model loaded successfully.")
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

SquareFeet = st.number_input("Enter the size of house", min_value=60, max_value=2400, step=50)    
Bedrooms = st.number_input("Enter the no of bedrooms", min_value=0, max_value=4, step=1)    
Bathrooms = st.number_input("Enter the no of bathrooms", min_value=0, max_value=6, step=1)    
Neighborhood = st.radio("Enter the neighborhood", ["Rural", "Urban", "Suburb"])
neighbor = 1 if Neighborhood == "Rural" else 2 if Neighborhood == "Urban" else 3

YearBuilt = st.number_input("Enter the number of year of construction", min_value=2000, max_value=2050, step=1)

if st.button("Predict Price"):
    price = model.predict([[SquareFeet, Bedrooms, Bathrooms, neighbor, YearBuilt]])
    st.write(f"The price for the flat with given details is Rs. {price[0]:,.2f}")

