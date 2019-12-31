import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options

def get_best(n):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=chrome_options)


    # go to github
    driver.get('https://finance.yahoo.com/trending-tickers')

    text_contents = [el.text for el in driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/section/div[2]")]
    all_li = []
    for text in text_contents:
        all_li = text.split("\n")
        #print(all_li)
    tickers = []
    for i in all_li:
        #print(i)
        space_after_ticker =i.find(" ")
        current_ticker = (i[:space_after_ticker]).upper()
        print(current_ticker)
        if current_ticker.count(".") <= 0 and current_ticker != 'SYMBOL':
            tickers.append(current_ticker)

    #print(tickers)

    best = tickers[:n]
    #print(best)

    # close window when doen
    driver.close()

    
    with open("stocks.json","w") as file:
        file.write(json.dumps(best))
    return best
best = get_best(5)
print(best)