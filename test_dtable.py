
import unittest


class Time:

    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def __init__(self, hour, minute, second):

        # Eliminate 1 out of 2 drawbacks from Simple Equivalence Partitioning
        # Type Checking
        if not isinstance(hour, int) or not isinstance(minute, int) or not isinstance(second, int):
            raise TypeError

        # H2, H3, M2, M3, S2, S3
        if hour < 0 or hour > 23 or minute < 0 or minute > 59 or second < 0 or second > 59:
            raise ValueError

        self.hour = hour
        self.minute = minute
        self.second = second

    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute

    def set_second(self, second):
        self.second = second

    def get_next_second(self):

        self.second += 1

        if (self.second >= 60):
            self.second = 0
            self.minute += 1

        if (self.minute >= 60):
            self.minute = 0
            self.hour += 1

        if (self.hour >= 24):
            self.hour = 0

        hour_str = f'0{self.hour}' if self.hour < 10 else self.hour
        minute_str = f'0{self.minute}' if self.minute < 10 else self.minute
        second_str = f'0{self.second}' if self.second < 10 else self.second
        return f'{hour_str}:{minute_str}:{second_str}'


class TestDecisionTable(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        time = Time(11, 29, 29)
        self.assertEqual(time.get_next_second(), '11:29:30')

    def test_2(self):
        time = Time(11, 29, 59)
        self.assertEqual(time.get_next_second(), '11:30:00')

    def test_3(self):
        time = Time(11, 59, 59)
        self.assertEqual(time.get_next_second(), '12:00:00')

    def test_4(self):
        time = Time(23, 59, 59)
        self.assertEqual(time.get_next_second(), '00:00:00')


if __name__ == '__main__':
    unittest.main()
