import time
from tkinter import *

from ui.imagebutton import ImageButton
import ui.dashboard

class Clock(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.clock_label = Label(self, font=('arial', 230, 'bold'), fg='gray10')
        self.clock_label.pack()

        dashboard_bt = ImageButton(container=self, path_to_img='images/dashboard.png', action=self.show_dashboard)
        dashboard_bt.pack()

        self.tick()

    def tick(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.clock_label.after(50, self.tick)

    def show_dashboard(self):
        self.pack_forget()
        dashboard = ui.dashboard.Dashboard(self.container)
        dashboard.pack()
