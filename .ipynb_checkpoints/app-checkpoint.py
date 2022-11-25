#Import streamlit 
import streamlit as st
import pandas as pd
from pandas.tseries.offsets import DateOffset
import daily_portfolio
import eth_helper
from ethereum import w3, generate_account, get_balance, send_transaction
from web3 import Web3
from datetime import datetime
import tax_events

#Define inc_tax bracket calculations
def inc_tax (total_y):
    #Tax Brackets
    bracket1=18200
    bracket2=45000
    bracket3=120000
    bracket4=180000
    rate1=0.19
    rate2=0.325
    rate3=0.37
    rate4=0.45
    '''calculates tax based on income enterd'''
    if total_y<=bracket1:
        return 0
    elif total_y<=bracket2:
        return (total_y-bracket1)*rate1
    elif total_y<=bracket3:
        return (total_y-bracket2)*rate2+(bracket2-bracket1)*rate1
    elif total_y<=bracket4:
        return (total_y-bracket3)*rate3+(bracket3-bracket2)*rate2+(bracket2-bracket1)*rate1
    elif total_y>bracket4:
        return (total_y-bracket4)*rate4+(bracket4-bracket3)*rate3+(bracket3-bracket2)*rate2+(bracket2-bracket1)*rate1


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
    #Drawing tax events
    st.write('Capital Gains Events for Financial Year')
    capital_gains_df = tax_events.calculate_yearly_gains(transactions_df)
    st.write(capital_gains_df)
    #Calculating capital gains
    capital_gain = capital_gains_df['net return'].sum()
    #Total Taxable Income
    total_y = income + capital_gain
    #Calculations
    st.write('Net Income: ')
    st.write(total_y-inc_tax(total_y))
    st.write(' ')
    st.write('Tax Paid: ') 
    st.write(inc_tax(total_y))
    st.write(' ')
    st.write('Effective Tax Rate: ')
    st.write(inc_tax(total_y)/total_y)


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

