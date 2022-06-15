# -*- coding: utf-8 -*-
"""
@author: Ali DİKME
"""
import json
import datetime
from threading import *
import time
from multiprocessing.pool import ThreadPool
global today_alarm


			
def objectToDict(obj):
    return {
        "type": str(obj.type),
        "date": str(obj.date),
        "lifeCycle": str(obj.lifeCycle),
        "message": str(obj.message)
    }


class Reminder:
    def __init__(self, type, date=4, lifeCycle=1, message=""):
        self.type = type
        self.date = date
        self.lifeCycle = lifeCycle
        self.message = message


class JsonDataBase:
    def __init__(self, fileName):
        self.filename = fileName

    def addNewJsonObject(self, newObject):
        with open(self.filename, 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            print(file_data)
            # Join new_data with file_data inside emp_details
            file_data["reminderNotes"].append(newObject)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)

    def deleteJsonObject(self, deletedDict):

        with open(self.filename, 'r') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            tempt_file_data = {
                "reminderNotes": [

                ]
            }

            for currentDict in file_data["reminderNotes"]:
                print(currentDict)
                if(deletedDict != currentDict):
                    # Join new_data with file_data inside emp_details
                    tempt_file_data["reminderNotes"].append(currentDict)

            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.

            with open(self.filename, 'w') as out_file:
                json.dump(tempt_file_data, out_file, indent=4)

    def readJsonFile(self):
        with open(self.filename, 'r') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            return file_data
    
        


def dictToReminderObject(Dict):
    datesInfo = Dict["date"].split(" ")
    datesInfoYears = datesInfo[0].split("-")
    datesInfoHours = datesInfo[1].split(":")
    newReminder = Reminder(str(Dict["type"]), datetime.datetime(
        int(datesInfoYears[0]), int(datesInfoYears[1]), int(datesInfoYears[2]), int(datesInfoHours[0]), int(datesInfoHours[1])), str(Dict["lifeCycle"]), str(Dict["message"]))
    return newReminder



constant = 'reminderNotes'
today = datetime.date.today()
print(today)
# DB object for handling the crud
DB = JsonDataBase("dates.json")


class StateManager:
    def __init__(self):
        self.state = DB.readJsonFile()
    
    def initStateCheck(self):
        while(1):
            for states in self.state[constant]:
                newState = dictToReminderObject(states)
                
                if(datetime.datetime.today() < newState.date):
                    print("hello")
                    today_alarm = [str(str(newState.date).split(" ")[1].split(":")[0]),str(str(newState.date).split(" ")[1].split(":")[1])]
                    print(today_alarm)
                    Threading(today_alarm[0],today_alarm[1],newState)
                    DB.deleteJsonObject(objectToDict(newState))
            break
                    
                
def Threading(par1,par2,par3):
	#t1=Thread(target=alarm,args=(par1,par2,par3))
	#t1.start()
    pool = ThreadPool(processes=1)
    global async_result
    async_result = pool.apply_async(alarm, (par1,par2,par3))
    
def alarm(par1,par2,par3):
	while(1):
		set_alarm_time = f"{par1}:{par2}"
		time.sleep(1)
		current_time = datetime.datetime.now().strftime("%H:%M")
		print(current_time,set_alarm_time)
		if (current_time == set_alarm_time):
			return par3
            


remind = Reminder("reminder", datetime.datetime(
    2022, 6, 15, 9, 47), 1, "take your medicine")
DB.addNewJsonObject(objectToDict(remind))

general=StateManager()
general.initStateCheck()
 # tuple of args for foo

# do some other stuff in the main process

#return_val = async_result.get()  # get the return value from your function.
#print(return_val.date)






