import pandas as pd

def getTransactionsByAccount(myaccount, w3):
    myaccount_transactions_df = pd.DataFrame(columns=['timestamp','currency','amount'])
    total_block_number = w3.eth.get_block_number()
    loop_range = list(range(1,total_block_number))
    for i in loop_range:  
        block = w3.eth.get_block(block_identifier=i,returnTransactionObjects=True)
        if (block != null & block.transactions != null):
            for tran in block.transactions:
                #check if the transaction is money sent from my wallet
                if myaccount == tran["from"]:
                    new_row = pd.DataFrame({'timestamp':[tran["timestamp"]], 'Currency':['ETH'], 'Amount':[-tran["value"]]}) 
                    myaccount_transactions_df = pd.concat([myaccount_transactions_df,new_row])
                #check if the transaction is money sent from my wallet
                elif myaccount == tran["to"]:
                    new_row = pd.DataFrame({'timestamp':[tran["timestamp"]], 'Currency':['ETH'], 'Amount':[tran["value"]]})
                    myaccount_transactions_df = pd.concat([myaccount_transactions_df,new_row])
    
    return myaccount_transactions_df