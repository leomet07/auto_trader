import requests
import json
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

querystring = {"region":"US","lang":"en","symbol":"AAPL"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "0246ddd03amsh5ebe249a9ff3841p1e581bjsn818c5c1931f7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
print(type(response.text))
data = json.loads(response.text)
print(type(data))
print(data.keys())

print("\n----------------\n")
#print(data['price'])

key_target = 'financialData'
print(data[key_target].keys())
print("////////////")


for key in data[key_target].keys():
    print("''''''''''")
    print(key)
    print(data[key_target][key])
    
fmt_current_price = data[key_target]['currentPrice']['fmt']
exc_current_price = data[key_target]['currentPrice']['raw']
print("\nCurrent Price: " + str(fmt_current_price))