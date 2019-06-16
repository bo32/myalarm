from tkinter import *

class ImageButton(Button):
    def __init__(self, container, path_to_img, action):
        super().__init__(container, command=action, borderwidth=0)
        
        photo = PhotoImage(file=path_to_img)
        
        self.config(image=photo)
        self.image=photo
        #self.pack()

