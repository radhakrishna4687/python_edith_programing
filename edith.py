#note: install modules for speach recogination,pyttsx3,os,dtaetime,webbrowser, wikipedia,smtplib,etc
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os


print('Initializing EDITH!...')

MASTER = 'Krishna'

engine = pyttsx3.Engine('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#writing a functiion called speak
#speak function will pronouced the string which is passed to it.
#function 1
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function 2: wishme
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0  and hour <12:
        speak('Good morning' + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)     
    else:
        speak('Good Evening' + MASTER)    
    speak('Hi Krishna, Iam ...EDITH.., how can i help you..!')
# These function take a command fro microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....!')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')    
        print("user said: ", {query})

    except Exception as e:
        print('Please say again,I am not understanding , what you said...!')
#Main program 

speak('Initializing  Edith...!')
wishMe()
takecommand()

