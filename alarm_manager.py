import json
from pathlib import Path

from alarm import Alarm

from data_manager import DataManager

class AlarmManager(DataManager):

    def __init__(self, json_filename = 'alarms.json', json_folderpath = Path.home() / '.myalarm'):
        super().__init__(json_filename, json_folderpath)

    def add_alarm(self, alarm):
        tmp = {}
        tmp['name'] = alarm.name
        tmp['hour'] = alarm.get_hour()
        tmp['minute'] = alarm.get_minute()
        self.add_item(alarm.name, tmp)

    def get_alarms(self):
        return self.get_items()

    # TODO: get_alarm_by_name() must return an instance of Alarm
    def get_alarm_by_name(self, name):
        self.print_alarms()
        for a in self.get_alarms():
            if a['name'] == name:
                return self.get_alarm_from_dict(a)
        return None

    def get_count_alarms(self):
        return len(self.get_alarms())

    def has_any_alarms(self):
        return self.get_count_alarms() > 0

    def print_alarms(self):
        if self.has_any_alarms():
            print('no alarms stored')
        else:
            for alarm in self.get_alarms():
                print(alarm)

    def get_alarm_from_dict(self, dic):
        alarm = Alarm(dic['name'])
        alarm.set_hour(dic['hour'])
        alarm.set_minute(dic['minute'])
        return alarm

    
    