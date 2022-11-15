#Import streamlit 

import streamlit as st
import pandas as pd

#write title 

st.title("Crypto Portfolio Dashboard and Personal Tax Calculation")

# Ask user to input their salary 

st.number_input("Input Salary")

#Ask user to upload transcation file 

file_uploader = st.file_uploader('Upload crypto transaction file (.csv)')

# Transform the upload file into dataframe 

#df = pd.read_csv(file_uploader)