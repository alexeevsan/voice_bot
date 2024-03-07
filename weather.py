import requests

API_KEY = '4bbf0d463f7de50fd6994660e176f272'
city_id = '1488754'
units = 'metric'

url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units={units}"


def get_weather():
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    return f'В Тюмени {temp} градусов'

