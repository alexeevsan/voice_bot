import requests


def chuck_say():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": "522b2384f8mshbe89721cb03c9d0p121185jsnffb274251280",
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()['value']


def translate():
    text = chuck_say()

    url = "https://text-translator2.p.rapidapi.com/translate"

    payload = {
        "source_language": "en",
        "target_language": "ru",
        "text": text
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "522b2384f8mshbe89721cb03c9d0p121185jsnffb274251280",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    data = response.json()

    return data['data']['translatedText']
