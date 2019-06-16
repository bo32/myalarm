from tkinter import *

from ui.imagebutton import ImageButton
import ui.clock 
import ui.alarms

class Dashboard(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        clock_bt = ImageButton(container=self, path_to_img='images/clock.png', action=self.show_clock)
        clock_bt.pack()

        alarm_bt = ImageButton(container=self, path_to_img='images/alarm.png', action=self.show_alarm)
        alarm_bt.pack()

        video_player_bt = ImageButton(container=self, path_to_img='images/video_player.png', action=self.show_video_player)
        video_player_bt.pack()

        settings_bt = ImageButton(container=self, path_to_img='images/settings.png', action=self.show_settings)
        settings_bt.pack()
        
        quit_bt = ImageButton(container=self, path_to_img='images/quit.png', action=self.quit)
        quit_bt.pack()
        
    def show_clock(self):
        self.pack_forget()
        clock = ui.clock.Clock(self.container)
        clock.pack()
    
    def show_video_player(self):
        # self.pack_forget()
        # clock = ui.video_player.VideoPlayer(self.container)
        # clock.pack()
        self.print_not_implemented_yet()

    def show_settings(self):
        self.print_not_implemented_yet()
    
    def show_alarm(self):
        self.pack_forget()
        alarms = ui.alarms.Alarms(self.container)
        alarms.pack()
        # self.print_not_implemented_yet()

    def quit(self):
        self.container.quit()

    def print_not_implemented_yet(self):
        print('not implemented yet')