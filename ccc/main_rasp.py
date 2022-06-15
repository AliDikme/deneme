# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 01:04:24 2022

@author: buubl
"""

import pyrebase
import speech_recognition as sr
import gtts
import os
import weather
import playsound


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
        filename = "audio1.wav"
        normal = ""
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            normal = text
            print(text)
        self.storage.child("Audio/audio.3gp").delete("audio.3gp")
        data = weather.get_weather_data("Muğla")
        print("Weather for:", data["region"])
        print("Now:", data["dayhour"])
        print(f"Temperature now: {data['temp_now']}°C")
        print("Description:", data['weather_now'])
        print("Precipitation:", data["precipitation"])
        print("Humidity:", data["humidity"])
        print("Wind:", data["wind"])
        print("Next days:")
        for dayweather in data["next_days"]:
            print("="*40, dayweather["name"], "="*40)
            print("Description:", dayweather["weather"])
            print(f"Max temperature: {dayweather['max_temp']}°C")
            print(f"Min temperature: {dayweather['min_temp']}°C")
        
        tts = gtts.gTTS(f"Sıcaklık şimdi: {data['temp_now']}°C",lang="tr")
        # save the audio file
        tts.save("hello.mp3")
        # play the audio file
        #playsound("hello.mp3")
        
        os.system('mpg321 hello.mp3 &')
    def uploadAuidoFile(self):
        self.storage.child("text.3gp").put("text.3gp")


app = App()
app.initApp()
app.processTheAuido()
