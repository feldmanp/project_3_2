def get_price(date,currency):
    pair=currency+"-AUD"
    data = yf.download(pair,date,date + timedelta(days=1))
    display(data.iloc[0,4])
    return data.iloc[0,4]

# Calling dataframe with date column

def calculate_yearly_gains(transactions_df):
    #1. adjust the dataframe
    transactions_df["date"]=transactions_df["timestamp"].str[:10]

    # Get prices and multiply by amount transacted + fill into table

    transactions_df['price'] = 0
    transactions_df['transaction value (AUD)'] = 0

    for index, row in transactions_df.iterrows():
        date = datetime.strptime(row["date"],'%Y-%m-%d')
        currency=row["currency"]
        amount=row["amount"]
        price=row["price"]
        transactions_df.loc[index,"price"]=get_price(date,currency)
        transactions_df.loc[index,"transaction value"]=get_price(date,currency)*amount

    #Split dataframes

    sell_df = transactions_df.loc[transactions_df["amount"]<0]
    buy_df = transactions_df.loc[transactions_df["amount"]>0]
    
    #Create tax event dataframe
    tax_events_df = pd.DataFrame(columns=['Sell Date','Return','Cost Base'])
    
    #Tax Events Cases
    
    for sell_index, sell_transaction in sell_df.iterrows():
    for buy_index, buy_transaction in buy_df.iterrows():
        if buy_transaction['currency'] == sell_transaction['currency']:
            
            # if buy transaction amount = sell transactions amount
            if buy_transaction['amount'] == -sell_transaction['amount']:
                new_row = pd.DataFrame({'sell date': [sell_transaction['date']], 'return': [-sell_transaction['transaction value']],'cost base': [-buy_transaction['transaction value']]})
                buy_df = buy_df.drop(index=buy_index)
                tax_events_df = pd.concat([new_row,tax_events_df])
            
            # if buy transaction amount > sell transactions amount
            elif buy_transaction['amount'] > -sell_transaction['amount']:
                cost_base = sell_transaction['amount']*buy_transaction['price']
                new_row = pd.DataFrame({'sell date': [sell_transaction['date']], 'return': [-sell_transaction['transaction value']],'cost base': [cost_base]})
                buy_df.at[buy_index,'amount'] = buy_transaction['amount'] + sell_transaction['amount']
                tax_events_df = pd.concat([new_row,tax_events_df])
            
            # if buy transaction amount < sell transactions amount
            
            elif buy_transaction['amount'] < -sell_transaction['amount']:
                sell_base = buy_transaction['amount']*sell_transaction['price']
                new_row = pd.DataFrame({'sell date': [sell_transaction['date']], 'return': [sell_base],'cost base': [-buy_transaction['transaction value']]})
                buy_df = buy_df.drop(index=buy_index)
                sell_transaction['amount'] = sell_transaction['amount'] + buy_transaction['amount']
                tax_events_df = pd.concat([new_row,tax_events_df])
                continue
            break 

    tax_events_df['net return']=0

    tax_events_df['net return'] = tax_events_df['return']+tax_events_df['cost base']
    
    return tax_events_df