from googlefinance import getQuotes
import json
import time
import os
import Tkinter as tk
import tkMessageBox


def get_update():
  current_Time = time.strftime("%H:%M")
  while current_Time != t1:
    current_Time = time.strftime("%H:%M")
  if current_Time == t1:
    stock = getQuotes(stock_input)
    print ('Stock: {0}'.format(stock[0]['StockSymbol']))
    print ('Current price: ${0}'.format(stock[0]['LastTradePrice']))


if __name__ == "__main__":
  stock_input = raw_input('What stock price would you like to check? ')
  stock = getQuotes(stock_input)
  print ('Stock: {0}'.format(stock[0]['StockSymbol']))
  print ('Current price: ${0}'.format(stock[0]['LastTradePrice']))

  check_price = raw_input('Would you like to set a time to check the price again? Yes or No: ')
  check_price = check_price.lower()
  while check_price != 'yes' and check_price != 'no':
    check_price = raw_input('Would you like to set a time to check the price again? Yes or No: ')
    check_price = check_price.lower()
  if check_price == 'yes':
    t1 = raw_input('At what time would you like to check (24h input hh:mm): ')
    alert = raw_input('Would you like to play an alert or get a pop up? alert or popup: ')
    alert = alert.lower()
    if alert == 'alert':
      get_update()
      os.system('say "You stock price was updated"') # will only work in MacOS
    elif alert == 'popup':
      get_update()
      root = tk.Tk()
      root.withdraw()
      tkMessageBox.showwarning('Stock Price Updated', 'Stock Price Updated!')
  elif check_price == 'no':
    print ('Thanks!')
    quit()
