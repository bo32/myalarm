from tkinter import *

# from alarm import Alarm

class AlarmTime(Frame):

    def __init__(self, container, alarm_manager):
        super().__init__(container)

        self.alarm_manager = alarm_manager

        self.hours = Scale(self, from_=0, to=23)
        self.hours.set(7)
        self.hours.pack()
        
        self.minutes = Scale(self, from_=0, to=59)
        self.minutes.set(30)
        self.minutes.pack()

    def get_minutes(self):
        return self.minutes.get()

    def get_hours(self):
        return self.hours.get()
    
    