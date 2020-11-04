import pyttsx3
import sys
import speech_recognition as sr
import webbrowser
import re
import datetime
from bs4 import BeautifulSoup as soup
import wikipedia


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk('Слушаю')


def command():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
        print(f'⊙_ರೃ Вы сказали: {task}')
    except:
        talk('Я вас не понимаю, повторите...')
        task = command()

    return task


def working(task):
    if 'привет' in task:
        talk('Здравствуйте, Бот вас слушает')
    elif 'как дела' in task:
        talk('У меня всё хорошо, а у вас?')
    elif 'спасибо' in task:
        talk('Всегда пожалуйста!')
    elif 'открой браузер' in task:
        talk('Введите сайт: ')
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            call = r.recognize_google(audio, language='ru-RU').lower()
            if re.search(r'\.', call):
                webbrowser.open_new_tab('https://' + call)
            elif re.search(r'\ ', call):
                webbrowser.open_new_tab('https://yandex.ru/search/?text=' + call)
            else:
                webbrowser.open_new_tab('https://yandex.ru/search/?text=' + call)
    elif 'открой сайт деревягин' in task:
        webbrowser.open_new_tab('https://derevyagin.market/')
    elif 'дата' in task:
        now = datetime.datetime.now()
        talk('Текущий год: %d' % now.year)
        talk('Текущий месяц: %d' % now.month)
        talk('Текущий день: %d' % now.day)
    elif 'время' in task:
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif 'пока' in task:
        talk('Досвидания, буду вас ждать'), sys.exit()


while True:
    working(command())
