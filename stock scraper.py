from site_html import *

stocks = ["GE"]

stocklist_data = []
for stock in stocks:
    print(stock)    
    stockdata = Stock_Data(stock)
    stocklist_data.append(stockdata)
for stock in stocklist_data:
    dir(stock.finviz_table_data)
    for item in stock.finviz_table_data:
        print(item + ": " + stock.finviz_table_data[item])
    


