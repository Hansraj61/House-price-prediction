import streamlit as st
import pandas as pd 
import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression
import pickle


st.image(r"C:\Users\dell\Downloads\innomatics.jpg",width=200)

st.title("HOUSE PRICE PREDICTION")
model = pickle.load(open(r"C:\Users\dell\lr.pkl","rb"))
#st.image(r"C:\Users\anees\python1\ino_img.jpeg")


SquareFeet = st.number_input("Enter the size of house",min_value = 60, max_value = 2400,step = 50)    
Bedrooms = st.number_input("Enter the no of bedrooms",min_value = 0,max_value = 4,step = 1)    
Bathrooms = st.number_input("Enter the no of bathrooms",min_value = 0,max_value = 6,step =1)    
Neighborhood = st.radio("Enter the neighborhood",["Rural","Urban","Suburb"])
neighbor = 1 if Neighborhood == "Rural" else 2 if Neighborhood == "Urban" else 3

YearBuilt = st.number_input("Enter the number of year of constructin",min_value = 2000, max_value = 2050,step = 1)

price = model.predict([[SquareFeet,Bedrooms,Bathrooms,neighbor,YearBuilt]])

st.write("The price for the flat with given detailes is Rs.",price)