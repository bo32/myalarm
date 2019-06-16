from data_manager import DataManager

class RadioManager(DataManager):

    def __init__(self):
        super().__init__('radios.json')

    def add(self, radio):
        self.radios.append(radio)
    
    # def update_json(self):
    #     pass