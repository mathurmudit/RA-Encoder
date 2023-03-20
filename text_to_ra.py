'''
This file's purpose is to take a speech input from the user and convert it to Courier's Code.
Input Type: Audio
Output Type: Text atm

For running this file:
    - may need to 'brew install flac'
    - may need to follow steps at:
        - https://stackoverflow.com/questions/73268630/error-could-not-build-wheels-for-pyaudio-which-is-required-to-install-pyprojec

'''

# these are some necessary imports for speech recognition
import sys
import subprocess
from subprocess import STDOUT, check_call
import os

# pip installations for necessary speech recognition packages
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'speechrecognition'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pyttsx3'])

# if you're running on an M1 Mac, you are going to need to do some extra setup
# that can be found here: https://stackoverflow.com/questions/73268630/error-could-not-build-wheels-for-pyaudio-which-is-required-to-install-pyprojec
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pyaudio'])

# this dictionary maps all characters to their Courier's Code representation
translate = {
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

# get input from the user
text = input("Enter the message you would like to convert to RA Courier's Code:")

# to reduce the number of entries in the 'translate' dictionary, use only lowercase letters
text = text.lower()

ra_text = ""

# reconstruct the 'text' input in 'ra_text' with the translated characters
for char in text:
    if char in translate:
        ra_text += (translate[char])
    # all lexicographical symbols that aren't alphabetical should remain unchanged
    else:
        ra_text += char



# ------------------------------------ HERE BEGINS THE SPEECH-TO-TEXT STUFF -------------------------

# these imports will give you warnings before running, but don't worry
# the packages are installed earlier in the script
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            SpeakText(MyText)
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")

print(ra_text)