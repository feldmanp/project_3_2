#Import streamlit 

import streamlit as st
import pandas as pd

#write title 

st.title("Crypto Portfolio Dashboard and Personal Tax Calculation")

# Ask user to input their salary 

income = st.number_input("Input Salary")

#Ask user to upload transcation file 

file_uploader = st.file_uploader('Upload crypto transaction file (.csv)')

# Transform the upload file into dataframe 

df = pd.read_csv(file_uploader)

# Displaying the user input CSV

st.write(df)

#For chart. 

#For Table of tax income content:

table = pd.DataFrame()

table["Financial year"] = pd.groupby(time_index_year)

table["Salary Income"] = income

table["Capital Gain/Loss from Crypto Investment"] = 

table["Capital Gain Income Tax (null if Capital Loss"] = 

st.table(table)