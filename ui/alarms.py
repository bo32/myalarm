from tkinter import *

from alarm_manager import *
from ui.imagebutton import ImageButton
from ui.list_button import AlarmButton
from ui.list_button import NewAlarmButton

import ui.alarm_add
import ui.dashboard

class Alarms(Frame):
    def __init__(self, container, alarm_manager=None):
        super().__init__(container)
        self.container = container

        if alarm_manager is None:
            self.alarm_manager = AlarmManager()
        else:
            self.alarm_manager = alarm_manager

        self.alarm_manager.print_alarms()
        print(self.alarm_manager.has_any_alarms())
        if self.alarm_manager.has_any_alarms():
            for a in self.alarm_manager.get_alarms():
                alarm_bt = AlarmButton(self, self.add_alarm, a['name'])
                alarm_bt.pack()
        
        new_alarm_bt = NewAlarmButton(self, self.add_alarm)
        new_alarm_bt.pack()
        # new_alarm_bt.pack(side="left", fill=X)

        dashboard_bt = ImageButton(container=self, path_to_img='images/dashboard.png', action=self.show_dashboard)
        dashboard_bt.pack(side="bottom")
    
    def add_alarm(self):
        self.pack_forget()
        new_alarm = ui.alarm_add.NewAlarm(self.container, self.alarm_manager)
        new_alarm.pack()

    def show_dashboard(self):
        self.pack_forget()
        dashboard = ui.dashboard.Dashboard(self.container)
        dashboard.pack()

