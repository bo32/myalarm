import unittest

from pathlib import Path

from alarm_manager import AlarmManager
from alarm import Alarm

class TestAlarmManager(unittest.TestCase):

    def test_has_any_items(self):
        dm = AlarmManager('removeme.json', Path.cwd() / 'tests' / 'resources')
        self.assertFalse(dm.has_any_alarms())
        
    def test_has_any_items_true(self):
        path = Path.cwd() / 'tests' / 'resources' / 'removeme.json'
        with path.open('w') as myfile:
            myfile.write('{ "test": { "name": "myalarm" } }')

        dm = AlarmManager('removeme.json', Path.cwd() / 'tests' / 'resources')
        self.assertTrue(dm.has_any_alarms())

    def test_add_alarm(self):
        dm = AlarmManager('removeme.json', Path.cwd() / 'tests' / 'resources')
        self.assertFalse(dm.has_any_alarms())
        
        dm.add_alarm(Alarm('test'))
        self.assertEqual(dm.get_count_alarms(), 1)
        
    def tearDown(self):
        path = Path.cwd() / 'tests' / 'resources' / 'removeme.json'
        path.unlink()

if __name__ == '__main__':
    unittest.main()