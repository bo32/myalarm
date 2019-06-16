from tkinter import *

import ui.alarms

class AlarmRepeat(Frame):
    def __init__(self, container, alarm_manager):
        super().__init__(container)
        self.container = container
        self.alarm_manager = alarm_manager

        Label(self, text='Widget for days to repeat the alarm').pack()


