# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyrebase
import speech_recognition as sr
import gtts
from playsound import playsound




"""
config = {
  "apiKey": "AIzaSyBcNW_6xpWvSdfoFTtVhWqA5AklQEgf7jw",
  "authDomain": "embed-ba315.firebaseapp.com",
  "projectId": "embed-ba315",
  "databaseURL":"xxx",
  "storageBucket": "embed-ba315.appspot.com",
  "serviceAccount":"ServiceAccount.json"
}


firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()


storage.child("text.wav").put("text.wav")

"""


filename = "text.wav"

# initialize the recognizer
r = sr.Recognizer()

normal=""
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    normal=text
    print(text)

# make request to google to get synthesis
tts = gtts.gTTS("bu bir normal konuşma",lang="tr")
# save the audio file
tts.save("hello.mp3")
# play the audio file
playsound("hello.mp3")



# gas leak detection notify

# room temperature control

# flood control

# healht monitoring

# special day reminder , medication reminder


# music player 


# setting an alarm

# weather during the day

