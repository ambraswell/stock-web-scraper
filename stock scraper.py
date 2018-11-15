from stock_data import *

list_of_stocks_to_get = ["GE", "F", "AMZN", "TSLA"]

def retrieve_stock_data(stock):
    return Stock_Data(stock)

def get_all_stocks_data(stocks):
    stocks_to_get = []
    for stock in stocks:
        print(stock)    
        stocks_to_get.append(retrieve_stock_data(stock))
    return stocks_to_get

def print_finviz_table_info_for_stocks(stocklist):
    for stock in stocklist:
        for item in stock.finviz_table_data:
            print(item + ": " + stock.finviz_table_data[item])

stocklist = get_all_stocks_data(list_of_stocks_to_get)
print_finviz_table_info_for_stocks(stocklist)
    


