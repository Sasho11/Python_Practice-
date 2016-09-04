import urllib, json

url = 'http://api.fixer.io/latest?base='
base_currency = raw_input('Which currency would you like to convert from? Type help for list of currencies: ')
base_currency = base_currency.upper()

while base_currency == 'HELP':
  print ('AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK','GBP','HKD','HRK','HUF',
         'IDR','ILS','INR','JPY','KRW','MXN','MYR','NOK','NZD','PHP','PLN','RON',
         'RUB','SEK','SGD','THB','TRY','ZAR','EUR')
  base_currency = raw_input('Which currency would you like to convert from? Type help for list of currencies: ')
  base_currency = base_currency.upper()

base = url+base_currency
response = urllib.urlopen(base)
data = json.loads(response.read())

to_currency = raw_input('Which currency would you like to convert to? ')
try:
  print ('Conversion rate: 1 {0} is {1} {2} '.format(base_currency,
          data['rates'][to_currency],to_currency))
except KeyError:
  print 'Sorry you did not choose a valid currency'
  quit()

custom_value_input = raw_input ('Would you like to convert custom values? Yes or No: ')
custom_value_input = custom_value_input.lower()
if custom_value_input == 'yes':
  custom_value = raw_input('What\'s the value? ')
  conversion_rate = float(custom_value) * data['rates'][to_currency]
  print ('Conversion rate: {0} {1} is {2} {3} '.format(custom_value, base_currency,
          conversion_rate,to_currency))
elif custom_value_input == 'no':
  print 'Thanks!'
else:
  print 'Sorry you did not type Yes or No! '
