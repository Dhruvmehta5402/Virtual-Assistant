import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak('Good Morining Sir')
    elif hour < 16:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')

    speak('Hello I am your Assistant. Please tell mew how may I help you')

# For listening and recognizing
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio,  language='en-in')
        print(f'User said: {query} \n')
    except Exception as e:
        print(e)
        print('say that again please')
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'google' in query:
            webbrowser.open('google.com')
            #chromium = webbrowser.get('chromium')
            #chromium.open_new_tab('google.com')
        elif 'quit' in query:
            exit()