import requests
import json

def get_price(sym):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

    querystring = {"region":"US","lang":"en","symbol":sym}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "0246ddd03amsh5ebe249a9ff3841p1e581bjsn818c5c1931f7"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)


    data = json.loads(response.text)

    key_target = 'financialData'

    fmt_current_price = data[key_target]['currentPrice']['fmt']
    exc_current_price = data[key_target]['currentPrice']['raw']
    print("\nCurrent Price of {}: ".format(sym) + str(fmt_current_price))

    return fmt_current_price

