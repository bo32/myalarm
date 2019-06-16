import json

from pathlib import Path

class DataManager():

    def __init__(self, json_filename, folder_path=Path.home() / '.myalarm'):
        json_folderpath = folder_path
        if not json_folderpath.exists():
            json_folderpath.mkdir()
        
        self.json_filepath = json_folderpath / json_filename
        if not self.json_filepath.exists():
            self.json_filepath.touch()
            self.json_filepath.write_text('{}')

        with self.json_filepath.open() as json_file:
            self.items = json.load(json_file)

    def get_items(self):
        return list(self.items.values())

    def add_item(self, key, value):
        self.items[key] = value
        self.update_json()

    def update_json(self):
        with open(self.json_filepath, 'w') as output:
            json.dump(self.items, output)