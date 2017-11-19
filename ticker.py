import requests
import time

print time.time()
ticker = requests.get('https://coinmate.io/api/ticker?currencyPair=LTC_BTC')
print ticker.text            
