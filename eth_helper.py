import pandas as pd
from datetime import datetime

def getTransactionsByAccount(myaccount, w3):
    myaccount_transactions_df = pd.DataFrame(columns=['timestamp','currency','amount'])
    total_block_number = w3.eth.get_block_number()
    loop_range = list(range(1,total_block_number))
    for i in loop_range:  
        block = w3.eth.get_block(block_identifier=i,full_transactions = True)
        if ( len(block.transactions) > 0 ):
            for tran in block.transactions:
                timestamp = block['timestamp']
                dt_object = datetime.fromtimestamp(timestamp)
                #check if the transaction is money sent from my wallet
                if myaccount == tran["from"]:
                    new_row = pd.DataFrame({'timestamp':[dt_object], 'currency':['ETH'], 'amount':[-tran["value"]*0.000000000000000001]}) 
                    myaccount_transactions_df = pd.concat([myaccount_transactions_df,new_row])
                #check if the transaction is money sent from my wallet
                elif myaccount == tran["to"]:
                    new_row = pd.DataFrame({'timestamp':[dt_object], 'currency':['ETH'],'amount':[tran["value"]*0.000000000000000001]})
                    myaccount_transactions_df = pd.concat([myaccount_transactions_df,new_row])

                   
    return myaccount_transactions_df
