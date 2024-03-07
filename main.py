import speech_recognition as sr  # speech to text
from gtts import gTTS  # text to speech
import playsound as ps  # play audio file
import os

import calculate as calc
import joke
import weather
import currency

working = True


def listen():
    # msg = input("Input command: ")
    print('\nГолосовой ввод:')
    rec = sr.Recognizer()
    try:
        with sr.Microphone() as sourse:
            speech = rec.listen(sourse, phrase_time_limit=3)
            msg = rec.recognize_google(speech, language='ru')
    except:
        msg = 'ошибка распознавания'

    action(msg)


def action(msg):
    print('Сообщение:', msg)

    if '+' in msg or '-' in msg or '/' in msg or 'х' in msg:
        speak(calc.calculate(msg))
    else:
        msg = msg.lower()
        if 'привет' in msg:
            speak('Здравствуйте!')
        elif 'пока' in msg:
            speak('Досвидания!')
            global working
            working = False
            # os.abort()
        elif 'курс' in msg:
            # (поддерживается рубль, евро, доллар)
            # Например:
            # курс рубля к доллару
            # курс рубля к евро
            # курс евро к доллару
            # курс евро к рублю
            # курс доллара к рублю
            # курс доллара к евро
            speak(currency.exchange_rate(msg))
        elif 'перевод' in msg:
            # (поддерживается рубль, евро, доллар)
            # Например:
            # перевод 100 евро в доллары
            # перевод 100 евро в рубль
            # перевод 100 евро в рубли
            # перевод 100 долларов в рубли
            # перевод 3 доллара в рубли
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
    print('Bot:', say)

    voice = gTTS(say, lang='ru')
    file = 'text.mp3'
    voice.save(file)
    ps.playsound(file)
    os.remove(file)


while working:
    listen()
