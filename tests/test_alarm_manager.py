import unittest

from pathlib import Path

from alarm_manager import AlarmManager

class TestAlarmManager(unittest.TestCase):

    def test_has_any_items(self):
        print(Path.cwd())
        dm = AlarmManager('test_alarms.json', Path.cwd() / 'tests')
        self.assertFalse(dm.has_any_alarms())

    def tearDown(self):
        path = Path.cwd() / 'tests' / 'test_alarms.json'
        path.unlink()

if __name__ == '__main__':
    unittest.main()