from tkinter import *
import pandas as pd

temp_order = []
order_data_list = []
order_names = []
order_prices = []
order_df = pd.DataFrame({'Number of Items' : pd.Series(dtype='int'),
                         'Subtotal' : pd.Series(dtype='float'),
                         'Tax' : pd.Series(dtype='float'),
                         'Total' : pd.Series(dtype='float'),
                         'Paid' : pd.Series(dtype='bool')
                         })

class OrderData:
    def add_item(self, item_name, price):
        global order_names
        global order_prices

        order_names.append(item_name)
        order_prices.append(price)
    
    def close_order(self):
        global order_names
        global order_prices
        global order_data_list
        global temp_order
        
        tempdict = dict(zip(order_names, order_prices))
        temp_order = tempdict
        order_data_list.append(tempdict)
        order_names.clear()
        order_prices.clear()
            
    def add_order_to_df(self, subtotal, tax, total):
        global order_data_list
        global temp_order
        global order_df
        
        n_items : int = 0
        for items in temp_order:
            n_items += 1
        
        order_df.loc[len(order_df.index)] = [n_items, subtotal, tax, total, False]
        print(order_df)

    def get_order_info(self):
        return order_df
    
        
        