import random

import speech_recognition as sr  # speech to text
from gtts import gTTS  # text to speech
import playsound as ps  # play audio file
import os

import calculate as calc
import joke
import weather
import currency


# Можно назвать бота своим именем, задать инициирущую команду и команду завершения работы
bot_name = 'Лиза'
initial_command = bot_name.lower()
final_command = f'{initial_command} пока'


# Добавьте свои приветствия
greetings = (
    'Чем могу помочь?',
    'Слушаю',
    'Да?'
)

'''
Распознаются команды:

1. Привет

2. Простой калькулятор

Например:
    2 + 2
    9 - 6
    5 * 5
    9 / 3
    
3. Курс (поддерживается рубль, евро, доллар)
          
Например:
    курс рубль доллар
    курс рубля к доллару
    курс рубля к евро
    курс евро к доллару
    курс евро к рублю
    курс доллара к рублю
    курс доллара к евро

4. Перевод (поддерживается рубль, евро, доллар), валюты можно склонять
            
Например:
    перевод 100 евро в доллары
    перевод 100 евро в рубль
    перевод 100 евро в рубли
    перевод 100 долларов в рубли
    перевод 3 доллара в рубли
    
5. шутка 

6. погода

7. рабочая папка - в функции action() задайте свой путь

'''


def initial():
    print(f'\nСкажите "{initial_command}":')
    rec = sr.Recognizer()
    try:
        with sr.Microphone() as sourse:
            speech = rec.listen(sourse)
            msg = rec.recognize_google(speech, language='ru')
            msg = msg.lower()

            if msg == final_command:
                os.abort()

            if initial_command in msg:
                while True:
                    listen()
            else:
                print(f'Вы сказали: {msg}')
                initial()
    except:
        print('Ошибка распознавания')
        initial()


def listen():
    greeting = greetings[random.randint(0, len(greetings))]
    print('')
    speak(greeting)

    rec = sr.Recognizer()
    try:
        with sr.Microphone() as sourse:
            speech = rec.listen(sourse, phrase_time_limit=3)
            msg = rec.recognize_google(speech, language='ru')
    except:
        initial()

    action(msg)


def action(msg):
    print('Сообщение:', msg)

    if len(msg.split()) == 3 and ('+' in msg or '-' in msg or '/' in msg or 'х' in msg):
        speak(calc.calculate(msg))
    else:
        msg = msg.lower()
        if msg == final_command:
            os.abort()
        elif 'привет' in msg:
            speak('Здравствуйте!')
        elif 'курс' in msg:
            speak(currency.exchange_rate(msg))
        elif 'перевод' in msg:
            speak(currency.converter(msg))
        elif 'шутка' in msg:
            speak(joke.translate())
        elif 'погода' in msg:
            speak(weather.get_weather())
        elif msg == 'рабочая папка':
            path = "D:\\YandexDisk\\top_academy"
            path = os.path.realpath(path)
            os.startfile(path)
        else:
            speak('Нет такой команды')


def speak(say):
    print(f'{bot_name}: {say}')

    voice = gTTS(say, lang='ru')
    file = 'text.mp3'
    voice.save(file)
    ps.playsound(file)
    os.remove(file)


initial()
