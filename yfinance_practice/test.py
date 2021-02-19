import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
import pandas_datareader as pdr #pandas_datareader used for financial market data
import pandas_datareader.data as data

#Ticker method of yfinance, creates ticker object
amzn=yf.Ticker('AMZN')
#print statement to show Ticker object
print(f"{amzn}\n")
#print statement to show Ticker object methods
print(f"{dir(amzn)}\n")
#prints stock information relating to amazon
print(f"{amzn.info}\n")

#alphabetically orders, stock information of above print statement
info = sorted([[k,v] for k,v in amzn.info.items()])

for k, v in info:
    print(f'{k} : {v}')

#shows how to use amazon history
print(f'{help(amzn.history)}\n')
#shows that the type of the amzn.history is a Pandas dataframe
print(f'{type(amzn.history())}\n')

#displays historical stock data for period 1d and interval of 1m
print(f'{amzn.history("1d","1m")}\n')
#period=1d, interval=15m
print(f'{amzn.history("1d","15m")}\n')
#period=1y interval=1d
print(f'{amzn.history("1y","1d")}\n')

#sets the limit of the max number of rows to display to 999, pandas method
pd.set_option('display.max_rows', 999)

#display historical stock data for interval of 1y
print(f'{amzn.history("1y")}\n')

#variable containing historical stock data of amazon over 1y period
amzn_history = amzn.history("1y")

#pandas method drop, used to drop Dividends and Stock Splits columns, think of inplace as replace for now
amzn_history.drop(columns=['Dividends', 'Stock Splits'],inplace=True)
print(f'{amzn_history}\n')

#using pandas rolling method to calculate 50 day and 200 day moving averages on close price
amzn_history['50MA'] = amzn_history.Close.rolling(50).mean()
amzn_history['200MA'] = amzn_history.Close.rolling(200).mean()

print(f'{amzn_history}\n')

#variable for amazon historical stock data over 2 year period
amzn_history = amzn.history("2y")
#as above, drop columns in square brackets
amzn_history.drop(columns=['Open', 'High', 'Low', 'Dividends', 'Stock Splits'],inplace=True)

#calculating moving averages
amzn_history['50MA'] = round(amzn_history.Close.rolling(50).mean(), 2)
amzn_history['200MA'] = round(amzn_history.Close.rolling(200).mean(), 2)
print(f'{amzn_history}\n')

#52 week high, 253 because amzn listed on nasdaq exchange which has 253 trading days
amzn_history['52WH'] = amzn_history.Close.rolling(253).max()
amzn_history['52WL'] = amzn_history.Close.rolling(253).min()

#calculates what percentage the current price is of the 52 week high
amzn_history['%ofH'] = round(amzn_history['Close'] / amzn_history['52WH'], 2)
print(f'{amzn_history}\n')

#slices data-frame to display only data over past year
amzn_history = amzn_history['2020-02-18':'2021-02-18']
print(f'{amzn_history}\n')

#using matplotlib to create graph of historical stock data --see https://www.grizzlypeaksoftware.com/articles?id=1m3W3llyJLy4YS5OpyyxBq for how to customise
amzn_history[['Close', '200MA', '50MA']].plot()
plt.show()

#shows method of pandas_datareader
print(f'{dir(pdr)}\n')

#we want to use data, print statement for help on data
print(f'{help(pdr.data)}')

#before we have been viewing data that is old, "historical" data, this is how you can get real time data
#this is historical data I think
amzn_data = data.get_data_yahoo('amzn')
print(f'{amzn_data}\n')

#this is how you get real time, also believe that yfinance .quote method may do same
amzn_quote = data.get_quote_yahoo('amzn')
print(f'{amzn_quote}\n')

#see from above print, there is 71 columns, to view columns use
print(f'{amzn_quote.columns}\n')