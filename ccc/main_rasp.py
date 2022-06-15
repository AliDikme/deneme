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
import serial


def isSubstring(s1, s2):
    M = len(s1)
    N = len(s2)

    # A loop to slide pat[] one by one
    for i in range(N - M + 1):

        # For current index i,
        # check for pattern match
        for j in range(M):
            if (s2[i + j] != s1[j]):
                break

        if j + 1 == M:
            return i

    return -1


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
            text = r.recognize_google(audio_data, language="tr-tr")
            normal = text
            print(text)

        city = ["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
                ]
        command1 = "hava durumu"
        command2 = "ev hakkında bilgi ver"
        # istanbul hava durumu
        # hatırlatıcı kur
        # alarm kur
        # müzik aç
        if(command2 == normal):
            print("hello")
            os.system('sudo rfcomm connect hci0  00:18:EF:00:04:38')
            ser = serial.Serial('dev/rfcomm0', 9600)
            while True:
                result = ser.readlines()
                print(result)

        elif(isSubstring(command1, normal)):
            cityText = normal.split(" ")[0]
            data = weather.get_weather_data(f"{cityText}")
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

            tts = gtts.gTTS(
                f"{cityText} içinde Sıcaklık : {data['temp_now']}°C", lang="tr")
            # save the audio file
            tts.save("hello.mp3")
            # play the audio file
            # playsound("hello.mp3")

            os.system('mpg321 hello.mp3 &')

    def uploadAuidoFile(self):
        self.storage.child("text.3gp").put("text.3gp")


app = App()
app.initApp()
app.processTheAuido()
