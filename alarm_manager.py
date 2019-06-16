import json
from pathlib import Path

from data_manager import DataManager

class AlarmManager(DataManager):

    def __init__(self, json_filename = 'alarms.json', json_folderpath = Path.home() / '.myalarm'):
        # super().__init__(Path.home() / '.myalarm', json_folderpath / 'alarms.json')
        super().__init__(json_filename, json_folderpath)
        # json_folderpath = 
        # # self.json_filepath = json_folderpath / 'alarms.json'
        # if not json_folderpath.exists():
        #     json_folderpath.mkdir()
        # if not self.json_filepath.exists():
        #     self.json_filepath.touch()
        #     self.json_filepath.write_text('{}')
        
        # with self.json_filepath.open() as json_file:
        #     self.alarms = json.load(json_file)

    # def update_json(self):
    #     with open(self.json_filepath, 'w') as output:
    #         json.dump(self.alarms, output)

    def add_alarm(self, alarm):
        tmp = {}
        tmp['name'] = alarm.name
        self.alarms[alarm.name] = tmp
        self.update_json()

    def get_alarms(self):
        return self.get_items()

    def has_any_alarms(self):
        return len(self.get_alarms()) > 0

    def print_alarms(self):
        if self.has_any_alarms():
            print('no alarms stored')
        else:
            for alarm in self.get_alarms():
                print(alarm)
    
    