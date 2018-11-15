from stock_data import *
import csv
import time

list_of_stocks_to_get = ["GE", "F"]

def write_to_csv(stocks):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file_name = "stocks for " + timestr + '.csv'
    myFile = open(file_name, 'w')
    for stock in stocks:        
        with open(file_name, 'w') as csvfile:
            myFields = ['symbol', 'url' ,'key', 'value']
            writer = csv.DictWriter(myFile, fieldnames=myFields)
            writer.writeheader()
            writer.writerow({'symbol' :  stock.symbol, 'url' : stock.finviz_url})
            for item in stock.finviz_table_data:
                writer.writerow({'symbol' : '', 'url': '', 'key' : item , 'value': stock.finviz_table_data[item]})
            writer.writerow({})
        #myFile.close()

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
#print_finviz_table_info_for_stocks(stocklist)
write_to_csv(stocklist)    


