class Alarm:
    def __init__(self, name):
        self.name = name
        self.hour = None
        self.minute = None
    
    def set_at(self, hour, minute):
        self.minute = minute
        self.hour = hour
    
    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute
