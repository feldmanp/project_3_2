#Import streamlit 
import streamlit as st
import pandas as pd
from pandas.tseries.offsets import DateOffset
import daily_portfolio
import eth_helper
from ethereum import w3, generate_account, get_balance, send_transaction
from web3 import Web3
from datetime import datetime


#Get address and account via Ganache

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


#write title 

st.title("Crypto Portfolio Dashboard and Personal Tax Calculation")

# Ask user to input their salary 

income = st.number_input("Input Salary")

############################################################



address = st.text_input("Input Account")
if st.button('Upload Transactions'):
    st.write(f'Transactions Uploaded from account: {address}') #displayed when the button is clicked
    df2 = eth_helper.getTransactionsByAccount(address, w3)
    st.markdown("First Ten Transactions From Your Account:")
    st.write(df2[0:10])



################################################

#Chart displaying daily crypto portfolio return

daily_portfolio_df = daily_portfolio.calculate_daily_portfolio("Resources/Transactions.csv")
st.markdown("Daily Portfolio Return")
st.bar_chart(daily_portfolio_df)

##############################################


#st.write(df[0:10])

#For chart. 

#For Table of tax income content:

#table = pd.DataFrame()

#Group by financial year 

#table["Financial year"] = df["Financial year"]


#table["Salary Income"] = income

#table["Capital Gain/Loss from Crypto Investment"] = 

#table["Capital Gain Income Tax (null if Capital Loss"] = 

#st.table(table) 

