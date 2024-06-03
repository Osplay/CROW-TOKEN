import time
import urllib.request
import json
import winsound



url_wemix_token = "https://api.wemixplay.com/info/v2/price-chart?symbol=CROW&range=1d"
sleep_time_request = 300
price_to_alert = 0.75

print("Script - V 00.00.00")

def wait(text=None):

    if text is not None:
        print(text)
    
    for waited_sleep_time in range(sleep_time_request, 0, -1):
        print("Next Check: {}".format(waited_sleep_time), end="\r")
        time.sleep(1)

def print_prices(prices):

    max_price = values['data']['chart'][0]['p']
    min_price = values['data']['chart'][0]['p']
    avg_price = 0
    total_price = 0
    num_price = 0

    for prices in values['data']['chart']:

        price = prices['p']

        if min_price > price:
            min_price = price

        if max_price < price:
            max_price = price

        total_price += price

        num_price += 1

    avg_price = total_price / num_price
    
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    print(f'Time: { date }')
    print(f'Avg price: {avg_price} | Max: { max_price } & Min: { min_price }')

    if avg_price > price_to_alert:
        alert(avg_price)

def alert(price):

    while(True):
        time.sleep(1)
        print(f'Price is: { price }')
        beep()

def beep():
    frequency = 1000
    duration = 500 
    winsound.Beep(frequency, duration)

while(True):


    request = urllib.request.Request(url_wemix_token)
    response = urllib.request.urlopen(request)

    data = response.read()
    values = json.loads(data)

    if values['ResultString'] != 'Success':
        wait("Error to access to prices...")
        continue
    
    print_prices(values)

    wait()

