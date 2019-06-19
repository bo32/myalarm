from tkinter import *

from alarm import Alarm

import ui.alarm_repeat
import ui.alarm_time
from ui.imagebutton import ImageButton

class NewAlarm(Frame):
    def __init__(self, container, alarm_manager):
        super().__init__(container)
        self.alarm_manager = alarm_manager
        self.container = container

        self.name_entry = Entry(self, text='Name')
        self.name_entry.pack()

        self.at = ui.alarm_time.AlarmTime(self, self.alarm_manager)
        self.at.pack()

        self.ar = ui.alarm_repeat.AlarmRepeat(self, self.alarm_manager)
        self.ar.pack()

        ok_bt = ImageButton(container=self, path_to_img='images/ok.png', action=self.confirm)
        ok_bt.pack()

        cancel_bt = ImageButton(container=self, path_to_img='images/back.png', action=self.back)
        cancel_bt.pack()

    def confirm(self):
        alarm = Alarm(name=self.name_entry.get())
        alarm.set_at(hour=self.at.get_hours(), minute=self.at.get_minutes())
        self.alarm_manager.add_alarm(alarm)
        self.pack_forget()
        alarms = ui.alarms.Alarms(self.container)
        alarms.pack()
    
    def back(self):
        self.pack_forget()
        alarms = ui.alarms.Alarms(self.container, self.alarm_manager)
        alarms.pack()