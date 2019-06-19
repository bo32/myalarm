from tkinter import *

import ui.alarms

from ui.day_button import *

DEFAULT_PADDING = 2

class AlarmRepeat(Frame):
    def __init__(self, container, alarm_manager):
        super().__init__(container)
        self.container = container
        self.alarm_manager = alarm_manager

        MondayButton(self).grid(row=0, column=0, padx=DEFAULT_PADDING)
        TuesdayButton(self).grid(row=0, column=1, padx=DEFAULT_PADDING)
        WednesdayButton(self).grid(row=0, column=2, padx=DEFAULT_PADDING)
        ThursdayButton(self).grid(row=0, column=3, padx=DEFAULT_PADDING)
        FridayButton(self).grid(row=0, column=4, padx=DEFAULT_PADDING)
        SaturdayButton(self).grid(row=0, column=5, padx=DEFAULT_PADDING)
        SundayButton(self).grid(row=0, column=6, padx=DEFAULT_PADDING)


