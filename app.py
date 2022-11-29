#Import statements
import streamlit as st
import pandas as pd
from pandas.tseries.offsets import DateOffset
import daily_portfolio
import eth_helper
from web3 import Web3
from datetime import datetime
import tax_events

################################################################
#Define inc_tax bracket for later calculations

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


######################################################################

#Get address and account via Ganache

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


#write title 

st.title("Crypto Portfolio Dashboard and Personal Tax Calculation")


################################################################

# Ask user to input their salary 

income = st.number_input("Input Salary")

############################################################

#Get transactions from the block and calculate daily portfoilio return 

address = st.text_input("Input Ethereum Account Address")
if st.button('Upload Transactions'):
    st.write(f'Transactions Uploaded from account: {address}') #displayed when the button is clicked
    transactions_df = eth_helper.getTransactionsByAccount(address, w3)
    daily_portfolio_df = daily_portfolio.calculate_daily_portfolio(transactions_df)
    st.markdown("Daily Portfolio Return")
    st.bar_chart(daily_portfolio_df)


    #########################################################################
    #Drawing tax events
    st.subheader('Capital Gains Events for Financial Year')
    st.text("(calculates tax based on income enterd)")
    capital_gain_df = tax_events.calculate_yearly_gains(transactions_df)
    #Calculating capital gains
    capital_gain = capital_gain_df['net return'].sum()
    #Total Taxable Income
    total_y = income + capital_gain
    #Calculations
    st.markdown(f'Net Income: $ {total_y-inc_tax(total_y)}')

    st.markdown(f'Tax Paid: $ {inc_tax(total_y)}') 

    st.markdown(f'Effective Tax Rate  is: {round(inc_tax(total_y)/total_y*100)} %')

    st.table(capital_gain_df)


###############################################################

