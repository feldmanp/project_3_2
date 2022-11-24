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

#Chart displaying daily crypto portfolio return



#######################################

# The Ethereum Account Address

#account = generate_account(w3)

#st.text("\n")
#st.text("\n")
#st.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
#st.write(account.address)


#######################################

# Create empty lists for later dataframe construction
time_1 = []
transaction_hash_1 = []
transaction_amount = []

#st.text("\n")
#st.text("\n")
#st.markdown("## Ethereum Transactions")

############################################################

#Get the total amount of blocks 

total_block_number = w3.eth.get_block_number()

loop = list(range(1,total_block_number))

for i in loop:
    
    #get transaction info from every transcation    
    transaction_1 = w3.eth.get_block(block_identifier=i)
    
    # obtain the time of the transaction 
    timestamp = transaction_1['timestamp']
    dt_object = datetime.fromtimestamp(timestamp)
    time_1.append(dt_object)
    
    #Transaction hash 
    #trans_hash = transaction_1['hash']
    #transaction_hash_1.append(trans_hash)
    
    # Obtain the transcation amount 
    trans_amount = w3.eth.get_transaction_by_block(i,0)
    amount = trans_amount['value']*0.000000000000000001 # in eth 
    transaction_amount.append(amount)
    
transactios = w3.eth.get_block('latest')

#######################################

# Transform the upload file into dataframe 

df = pd.DataFrame() 
df['Date'] = time_1
df['Amount in Eth'] = transaction_amount

# Displaying first ten transactions
st.markdown("First 10 transcations in your block chain")
st.write(df[0:10])



address = st.text_input("Input Account")
if st.button('Upload Transactions'):
    st.write(f'Transactions Uploaded from account: {address}') #displayed when the button is clicked
    transactions_df = eth_helper.getTransactionsByAccount(address, w3)
    st.write(transactions_df)
    daily_portfolio_df = daily_portfolio.calculate_daily_portfolio(transactions_df)
    st.markdown("Daily Portfolio Return")
    st.bar_chart(daily_portfolio_df)
    
    
#######################################
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

