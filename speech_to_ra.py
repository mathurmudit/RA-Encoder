'''
This file's purpose is to take a speech input from the user and convert it to Courier's Code.
Input Type: Audio from Microphone
Output Type: Text (Courier's Code Representation)

For running this file:
    - may need to 'brew install flac'
    - may need to follow steps at:
        - https://stackoverflow.com/questions/73268630/error-could-not-build-wheels-for-pyaudio-which-is-required-to-install-pyprojec

All dependencies can be found in requirements.txt, which should be pip install -r'd before
running locally.

Your machine needs to be connected to the internet in order to run recognize_google().
'''

from re import M
import sys
import subprocess
from subprocess import STDOUT, check_call
import os
import speech_recognition as sr
import pyttsx3

couriers_code = {
    'a': '11',
    'b': '12',
    'c': '13',
    'd': '14',
    'e': '15',
    'f': '16',
    'g': '21',
    'h': '22',
    'i': '23',
    'j': '24',
    'k': '25',
    'l': '26',
    'm': '31',
    'n': '32',
    'o': '33',
    'p': '34',
    'q': '35',
    'r': '36',
    's': '41',
    't': '42',
    'u': '43',
    'v': '44',
    'w': '44',
    'x': '45',
    'y': '46',
    'z': '41',
    ' ': ' ',
}

# Initialize the recognizer to ensure it returns when it hears silence
r = sr.Recognizer()
r.dynamic_energy_threshold = False
r.energy_threshold = 400

def listen_and_return_text():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
            
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 3)

    try:            
            print("Recognizing...")
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            print("English text heard: ",MyText)
            return MyText

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
            
    except sr.UnknownValueError:
        print("unknown error occurred")

def english_to_couriers_code(MyText):
    ra_text = ""
    for char in MyText:
        if char in couriers_code:
            ra_text += (couriers_code[char])
        # all symbols that aren't alphabetical should remain unchanged
        else:
            ra_text += char
    return ra_text

MyText = listen_and_return_text()
ra_text = english_to_couriers_code(MyText)

print("Courier's Code Translation: ",ra_text)
