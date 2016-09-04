from googlefinance import getQuotes
import json


stock_input = raw_input('What stock price would you like to check? ')
stock = getQuotes(stock_input)
print ('Stock: {0}'.format(stock[0]['StockSymbol']))
print ('Current price: ${0}'.format(stock[0]['LastTradePrice']))

