from tkinter import *

class ListButton(Button):
    def __init__(self, container, path_to_img, action, text):
        image = PhotoImage(file=path_to_img)
        super().__init__(container, text=text, image=image, compound="left", command=action, borderwidth=0)
        self.image=image

class NewAlarmButton(ListButton):
    def __init__(self, container, action):
        super().__init__(container, path_to_img='images/64/add.png', text="Add an alarm", action=action)

class AlarmButton(ListButton):
    def __init__(self, container, action, text):
        super().__init__(container, path_to_img='images/64/bell.png', text=text, action=action)