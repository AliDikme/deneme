# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 01:04:24 2022

@author: buubl
"""

import pyrebase
import speech_recognition as sr
import gtts
import os


class App:
    def initApp(self):
        config = {
            "apiKey": "AIzaSyCYexbzCLj43gftN0JHARygYiGiAQzWU4U",
            "authDomain": "virtual-assistant-9042e.firebaseapp.com",
            "projectId": "virtual-assistant-9042e",
            "storageBucket": "virtual-assistant-9042e.appspot.com",
            "databaseURL": "xxx",
            "serviceAccount": "ServiceAccount.json"
            }
        
        firebase_storage = pyrebase.initialize_app(config)
        self.storage = firebase_storage.storage()
    def processTheAuido(self):
        self.storage.child("Audio/audio.3gp").download("audio.3gp")
        os.system('ffmpeg -i ./audio.3gp ./audio1.wav')
        r = sr.Recognizer()
        filename="audio1.wav"
        normal=""
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            normal=text
            print(text)
    def uploadAuidoFile(self):
        self.storage.child("text.3gp").put("text.3gp")
        


app = App()
app.initApp()
app.processTheAuido()
