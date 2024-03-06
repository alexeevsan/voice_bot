import speech_recognition as sr     # speech to text
from gtts import gTTS               # text to speech
import playsound as ps              # play audio file
import os
import operator


working = True


def listen():
    # msg = input("Input command: ")
    print('Голосовой ввод:')
    rec = sr.Recognizer()
    try:
        with sr.Microphone() as sourse:
            speech = rec.listen(sourse, phrase_time_limit=3)
            msg = rec.recognize_google(speech, language='ru')
    except:
        msg = 'ошибка распознавания'

    action(msg)


def calculate(msg):
    try:
        a, oper, b = msg.replace(',', '.').split(' ')
    except:
        return msg

    a = float(a) if '.' in a else int(a)
    b = float(b) if '.' in b else int(b)

    ops = {
        '+': operator.add,
        '-': operator.sub,
        'х': operator.mul,
        '/': operator.truediv
    }

    return str(ops[oper](a, b))


def action(msg):
    print('Сообщение:', msg)

    if '+' in msg or '-' in msg or '/' in msg or 'х' in msg:
        speak(calculate(msg))
    else:
        msg = msg.lower()
        if 'привет' in msg:
            speak('Здравствуйте!')
        elif 'пока' in msg:
            speak('Досвидания!')
            global working
            working = False
            # os.abort()
        elif 'как дела' in msg:
            speak('Хорошо!')
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
