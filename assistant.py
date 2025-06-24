import speech_recognition as sr 
import pywhatkit
import pyttsx3
import os
import sys
import wikipedia
import pyjokes
import datetime

#initialization tts engine(interface to text to speech engine(tts) default:- SAPI5 on Windows It does not require an internet connection, unlike other cloud-based TTS services.)
speech_engine=pyttsx3.init()
speech_engine.setProperty('rate',170)#setting speed default:200
voices=speech_engine.getProperty('voices')
#retrieves all available voices installed on your system.
#The result is a list of voice objects. Each voice has attributes like id, name, language, gender, etc.
speech_engine.setProperty('voice',voices[1].id)

def talk(text):
    print("ANYA:",text)
    speech_engine.say(text)
    speech_engine.runAndWait()

def take_command():
    listener=sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        voice=listener.listen(source)
    try:
        command=listener.recognize_google(voice)
        command=command.lower()
        print("You said:",command)
        
