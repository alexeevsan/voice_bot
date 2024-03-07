import requests

currency_list = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR'
}


def plural(currency, qty):
    qty = int(qty)
    declensions = {
        'рубль': ('рубль', 'рубля', 'рублей'),
        'доллар': ('доллар', 'доллара', 'долларов'),
        'евро': ('евро', 'евро', 'евро')
    }

    cases = [2, 0, 1, 1, 1, 2]
    declension = declensions[currency]

    return declension[2 if 4 < qty % 100 < 20 else cases[qty % 10 if qty % 10 < 5 else 5]]


def get_currency_name(currency):
    result = ''
    for key in currency_list:
        if currency[0:2] in key:
            result = key

    return result


def supported_currencies():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"

    headers = {
        "X-RapidAPI-Key": "522b2384f8mshbe89721cb03c9d0p121185jsnffb274251280",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()


def get_exchange(cur1, cur2, amount=1):
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {f"from": {currency_list[cur1]}, "to": currency_list[cur2], "amount": {amount}}

    headers = {
        "X-RapidAPI-Key": "522b2384f8mshbe89721cb03c9d0p121185jsnffb274251280",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    return requests.get(url, headers=headers, params=querystring)


def exchange_rate(msg):
    msg = msg.replace(' к ', ' ')
    try:
        text, cur1, cur2 = msg.split(' ')

        req_cur1 = get_currency_name(cur1)
        req_cur2 = get_currency_name(cur2)

        if req_cur1 not in currency_list or req_cur2 not in currency_list:
            return 'Валюта не поддерживается'
    except:
        return 'Нет такой команды'

    response = get_exchange(req_cur1, req_cur2)

    curs = response.json()['result']['convertedAmount']

    return f'Курс {cur1} к {cur2} составляет {round(float(curs), 2)}'


def converter(msg):
    msg = msg.replace(' в ', ' ')
    try:
        text, amount, cur1, cur2 = msg.split(' ')

        cur1 = get_currency_name(cur1)
        cur2 = get_currency_name(cur2)

        if cur1 not in currency_list or cur2 not in currency_list.keys():
            return 'Валюта не поддерживается'
    except:
        return 'Нет такой команды'

    response = get_exchange(cur1, cur2, amount)

    exchanged = response.json()['result']['convertedAmount']
    exchanged = round(float(exchanged), 2)

    return f'{amount} {plural(cur1, amount)} это {exchanged} {plural(cur2, exchanged)}'
