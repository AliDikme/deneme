# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 01:04:24 2022

@author: buubl
"""

import pyrebase
#import speech_recognition as sr
#import gtts
import os


class App:
    def initApp(self):
        config = {
            "apiKey": "AIzaSyD1TSdSR3RLgsatMqISgeQmmI9QacWu5-I",
            "authDomain": "embed-b83a1.firebaseapp.com",
            "projectId": "embed-b83a1",
            "databaseURL": "xxx",
            "storageBucket": "embed-b83a1.appspot.com",
            "serviceAccount": "ServiceAccount.json"
        }
        
        firebase_storage = pyrebase.initialize_app(config)
        self.storage = firebase_storage.storage()
    def processTheAuido(self):
        self.storage.child("text.3gp").download("text.3gp")
        os.system('ffmpeg -i path/to/3gp.3gp path/to/wav.wav')
    def uploadAuidoFile(self):
        self.storage.child("text.3gp").put("text.3gp")
        


app = App()
app.initApp()
app.processTheAuido()


"""

    """