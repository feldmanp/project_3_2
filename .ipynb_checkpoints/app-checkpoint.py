#Import streamlit 

import streamlit as st
import pandas as pd
from pandas.tseries.offsets import DateOffset
import daily_portfolio
# Import the functions from ethereum.py
from ethereum import w3, generate_account, get_balance, send_transaction
from web3 import Web3


#Get address and account via Ganache

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


#write title 

st.title("Crypto Portfolio Dashboard and Personal Tax Calculation")

# Ask user to input their salary 

income = st.number_input("Input Salary")

daily_portfolio_df = daily_portfolio.calculate_daily_portfolio("Resources/Transactions.csv")
st.bar_chart(daily_portfolio_df)

#######################################

# The Ethereum Account Address

#account = generate_account(w3)


#st.text("\n")
#st.text("\n")
#st.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
#st.write(account.address)


#######################################

time_1 = []
transaction_hash_1 = []
transaction_amount = []

# An Ethereum Transaction
#st.text("\n")
#st.text("\n")
#st.markdown("## An Ethereum Transaction")

# Create inputs for the receiver address and ether amount
#receiver = st.text_input("Input the receiver address")
#ether = st.number_input("Input the amount of ether")

# Create a button that calls the `send_transaction` function and returns the transaction hash
#if st.button("Send Transaction"):

 #   transaction_hash = send_transaction(w3, account, receiver, ether)
#
    # Display the Etheremum Transaction Hash
 #   st.text("\n")
  #  st.text("\n")
   # st.markdown("## Ethereum Transaction Hash:")

    #st.write(transaction_hash)
    #transaction_hash_1.append(transaction_hash)
    #transaction_amount.append(ether)
    
# Add timestamp of the transcation 

    #tx = transaction_hash
#   block_number = w3.eth.getTransaction(tx).blockNumber
 #   time = w3.eth.getBlock(block_number).timestamp
  #  time_1.append(time)
    
transactios = w3.eth.get_block('latest')

st.write(transactios)

# Enter your account address

account = st.text_input("Enter your account address")

account_balance = w3.eth.get_balance(account, block_identifier=2)

st.write(account_balance)

#######################################

# Transform the upload file into dataframe 

df = pd.DataFrame(transaction_hash_1,transaction_amount,time_1) 

#df["Financial year"] = df.index.map(lambda d: d.year + 1 if d.month > 6 else d.year)

# Displaying the user input CSV


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

