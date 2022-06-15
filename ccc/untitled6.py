# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:23:49 2022

@author: buubl
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('ServiceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
