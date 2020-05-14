from datetime import datetime
import os
import pytz
import requests
import math
API_KEY = '8d8b46a7eec6f34f2d50a77be8cf6053'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
