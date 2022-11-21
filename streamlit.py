#Import streamlit 

import streamlit as st
import pandas as pd
from pandas.tseries.offsets import DateOffset

#write title 

st.title("Crypto Portfolio Dashboard and Personal Tax Calculation")

# Ask user to input their salary 

income = st.number_input("Input Salary")

#Ask user to upload transcation file 

file_uploader = st.file_uploader('Upload crypto transaction file (.csv)')

# Transform the upload file into dataframe 

df = pd.read_csv(file_uploader,
index_col= "Date",
infer_datetime_format=True, 
parse_dates=True)

df["Financial year"] = df.index.map(lambda d: d.year + 1 if d.month > 6 else d.year)

# Displaying the user input CSV


st.write(df[0:10])

#For chart. 

#For Table of tax income content:

table = pd.DataFrame()

#Group by financial year 

table["Financial year"] = df["Financial year"]


table["Salary Income"] = income

#table["Capital Gain/Loss from Crypto Investment"] = 

#table["Capital Gain Income Tax (null if Capital Loss"] = 

st.table(table) 