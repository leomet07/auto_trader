import requests
import json
from matplotlib import pyplot as plt
import math
from linear import linear
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"

querystring = {"interval":"60m","region":"US","symbol":"QCOM","lang":"en","range":"5d"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "0246ddd03amsh5ebe249a9ff3841p1e581bjsn818c5c1931f7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)['chart']['result'][0]

#print(data.keys())
timestamps = data['timestamp']
#print(data['indicators'].keys())
quotes = data['indicators']['quote'][0]

quotes_high = quotes['high']
print(len(quotes_high))
print("Current_price: " + str(quotes_high[-1]))
#removing all none types
quotes_high = [i for i in quotes_high if i] 
'''
checked_quotes = []
for i in range(len(quotes_high)):

    if not(i):
        print(i)
        print("next " + str( checked_quotes[i+1]))
        checked_quotes.append(quotes_high[i-1])
    else:
        checked_quotes.append(quotes_high[i])
quotes_high = checked_quotes
'''
#print(quotes_high)
a = []


for i in range(len(quotes_high)):
    a.append(i)

#last val is current date
#print(quotes_high[-1])
#first val is all the way back
#print(quotes_high[0])
m,b = linear(a,quotes_high,plot=True)
if m > 0:
    #in upward trend
    if m > 0.15 and m < 0.4:
        print("medium (improving) upward trend")
    elif m >= 0.4:
        print("extremley high trend")


