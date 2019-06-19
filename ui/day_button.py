from tkinter import *

class DayButton(Button):
    def __init__(self, container, day):
        super().__init__(container, text=day, width=8, height=5)

class MondayButton(DayButton):
    def __init__(self, container):
        super().__init__(container, day='Monday')
        
class TuesdayButton(DayButton):
    def __init__(self, container):
        super().__init__(container, day='Tuesday')
        
class WednesdayButton(DayButton):
    def __init__(self, container):
        super().__init__(container, day='Wednesday')
        
class ThursdayButton(DayButton):
    def __init__(self, container):
        super().__init__(container, day='Thursday')
        
class FridayButton(DayButton):
    def __init__(self, container):
        super().__init__(container, day='Friday')
        
class SaturdayButton(DayButton):
    def __init__(self, container):
        super().__init__(container, day='Saturday')
        
class SundayButton(DayButton):
    def __init__(self, container):
        super().__init__(container, day='Sunday')