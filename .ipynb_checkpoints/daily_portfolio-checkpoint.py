import pandas as pd
from datetime import datetime,timedelta
import yfinance as yf

def get_price(date,currency):
    pair=currency+"-AUD"
    data = yf.download(pair,date,date + timedelta(days=1))
    return data.iloc[0,4]
    
def calculate_daily_value(date,summary_portfolio_df):
    amount_aud = 0
    for index, row in summary_portfolio_df.iterrows(): 
        aud_price = get_price(date,index)
        amount_aud += row['amount'] * aud_price
    
    return amount_aud

def update_holdings(current_holdings, new_transactions):
    for index, row in new_transactions.iterrows():
        #parse the row
        date = datetime.strptime(row['date'], '%Y-%m-%d')
        currency = row['currency']
        amount = row['amount']
        
        if not currency in current_holdings.index:
            new_row = pd.DataFrame({'currency':[currency], 'amount':[amount]})
            new_row.set_index('currency',inplace=True)
            current_holdings = pd.concat([current_holdings,new_row])
        else:
            current_holdings.loc[currency, 'amount'] += amount 
    
    #return the updated holdings
    return current_holdings

def calculate_daily_portfolio(transactions_df):
    #1. adjust the dataframe
    transactions_df["date"]=transactions_df["timestamp"].str[:10]
    
    #2. Generate all dates
    start_date=transactions_df.iloc[0,1]
    end_date=transactions_df.iloc[len(transactions_df)-1,1]
    portfolio_daily_view = pd.DataFrame({'date': pd.date_range(start_date, end_date), 'AUD':0})
    portfolio_daily_view['date']=portfolio_daily_view['date'].dt.strftime('%Y-%m-%d')
    portfolio_daily_view.set_index('date',inplace=True)
    
    
    #3. generate summary of holdings
    holdings_df = pd.DataFrame(columns=['currency','amount'])
    holdings_df.set_index('currency',inplace=True)

    #4. For every date
    for index, row in portfolio_daily_view.iterrows():    
        #prepare data
        date = datetime.strptime(index, '%Y-%m-%d')

        #4.1 Check if transactions exists: 
        daily_transactions = transactions_df.loc[transactions_df['date'] == index]
        # if yes, update total balance of coins
        if len(daily_transactions) > 0:
            holdings_df=update_holdings(holdings_df, daily_transactions)

        #4.2. Calcualte AUD balance
        portfolio_daily_view.loc[index,'AUD'] = calculate_daily_value(date,holdings_df)

    return portfolio_daily_view