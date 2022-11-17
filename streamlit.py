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

#Ask user to input the month until financial year (30 Jun each year)

until_financial_year = st.number_input("Input the number of months from the beginning of your transcation date to the end of the financial year (30 Jun))")

# Transform the upload file into dataframe 

df = pd.read_csv(file_uploader,
index_col= "Date",
infer_datetime_format=True, 
parse_dates=True)

# Displaying the user input CSV

st.text("First ten rows of user input data")

st.write(df[0:10])

#For chart. 

#For Table of tax income content:

table = pd.DataFrame()

#Calculate for certain period of time (eg. Each financial year, each quater)

table["Financial year"] = df.index.min() + DateOffset(months=until_financial_year)


#table["Salary Income"] = income

#table["Capital Gain/Loss from Crypto Investment"] = 

#table["Capital Gain Income Tax (null if Capital Loss"] = 

st.table(table)