import streamlit as st
import numpy as np
import pickle
import os

# Load the model using a relative path
model_path = os.path.join(os.path.dirname(__file__), "lr.pkl")
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Error: Model file '{model_path}' not found.")
    st.stop()
except Exception as e:
    st.error("Error loading the model:")
    st.error(e)
    st.stop()

st.image("innomatics.jpg")
# Title and image
st.title("HOUSE PRICE PREDICTION")

# Specify the path to your image file using __file__ method
#image_path = os.path.join(os.path.dirname(__file__), "ino_img.jpg")

# Input fields
SquareFeet = st.number_input("Enter Area of house in square feet", min_value=2400, max_value=6000, step=50)
Bedrooms = st.number_input("Enter the number of bedrooms", min_value=0, max_value=6, step=1)
Bathrooms = st.number_input("Enter the number of bathrooms", min_value=0, max_value=6, step=1)
Neighborhood = st.radio("Select type of neighbourhood", ['Rural', 'Urban', 'Suburb'])
neighbor = 1 if Neighborhood == "Rural" else 2 if Neighborhood == "Urban" else 3
YearBuilt = st.number_input("Enter year of Construction of property", min_value=2020, max_value=2070, step=1)

# Prediction
if st.button("PREDICT PRICE"):
    try:
        price = model.predict([[SquareFeet, Bedrooms, Bathrooms, neighbor, YearBuilt]])
        st.write("The price for the flat with given details is Rs.", price[0])
    except Exception as e:
        st.error("An error occurred during prediction:")
        st.error(e)
