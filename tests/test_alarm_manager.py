import unittest

from pathlib import Path

from alarm_manager import AlarmManager
from alarm import Alarm

class TestAlarmManager(unittest.TestCase):

    def test_has_any_items(self):
        self.assertFalse(self.dm.has_any_alarms())
        
    def test_has_any_items_true(self):
        self.assertFalse(self.dm.has_any_alarms())

        self.dm.add_alarm(Alarm('test'))
        self.assertTrue(self.dm.has_any_alarms())

    def test_add_alarm(self):
        self.assertFalse(self.dm.has_any_alarms())
        
        alarm = Alarm('7:30')
        alarm.set_at(hour='7', minute='30')

        self.dm.add_alarm(alarm)
        self.assertEqual(self.dm.get_count_alarms(), 1)
        
        candidate = self.dm.get_alarm_by_name('7:30')
        self.assertTrue(candidate is not None)
        self.assertEqual(candidate.get_hour(), '7')
        self.assertEqual(candidate.get_minute(), '30')

    def test_get_alarm_by_name(self):
        alarm = Alarm('test')
        self.dm.add_alarm(alarm)
        candidate = self.dm.get_alarm_by_name('test')
        self.assertTrue(isinstance(candidate, Alarm))

        self.assertTrue(candidate is not None)
    
    def setUp(self):
        self.dm = AlarmManager('removeme.json', Path.cwd() / 'tests' / 'resources')
        
    def tearDown(self):
        path = Path.cwd() / 'tests' / 'resources' / 'removeme.json'
        path.unlink()

if __name__ == '__main__':
    unittest.main()