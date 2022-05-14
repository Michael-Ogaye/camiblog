import requests,json


import threading
cnt=1

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()
        cnt=cnt+1
        if cnt==100:
            continue

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
        return quote