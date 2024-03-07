import requests

url = "https://cat14.p.rapidapi.com/v1/images/search"

headers = {
    "x-api-key": "live_tkfn5Qu13T9qimIfGmAxBAFooC12t7GvENwLXIoJQRTgUv83zQ8mjz5cSpzahmyK",
    "X-RapidAPI-Key": "522b2384f8mshbe89721cb03c9d0p121185jsnffb274251280",
    "X-RapidAPI-Host": "cat14.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
