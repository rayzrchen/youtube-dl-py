import unittest
from datetime import datetime
from pathlib import Path


class TestDemo(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_is_upper(self):
        self.assertEqual('Foo'.isupper(), False)
        self.assertEqual('FOO'.isupper(), True)

    def test_date_time(self):
        self.assertNotEqual(datetime.now(), datetime.utcnow(), 'this is the message')

    def test_path(self):
        temp_txt_ = Path('nodejs') / 'temp.txt'
        self.assertEqual(temp_txt_, Path('nodejs/temp.txt'))
        self.assertEqual(temp_txt_.exists(), False)
        self.assertEqual(temp_txt_.absolute(),
                         Path(r'C:\Users\rayzr\Documents\IdeaProjects\youtube-dl-py\nodejs\temp.txt'))

    def test_time_stamp(self):
        tstr = '2019-06-18T01:02:03'
        timestamp = self.convert_utc_time_str_to_utc_timestamp(tstr)
        print(timestamp)
        print(self.convert_utc_timestamp_to_utc_time_str(timestamp))

    def convert_utc_time_str_to_utc_timestamp(self, utc_time_str: str) -> int:
        gap = (datetime.now() - datetime.utcnow()).seconds
        return int(datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%S').timestamp() + gap) * 1000

    def convert_utc_timestamp_to_utc_time_str(self, utc_timestamp: int) -> str:
        utcfromtimestamp = datetime.utcfromtimestamp(utc_timestamp / 1000)
        return utcfromtimestamp.strftime('%Y-%m-%dT%H:%M:%S')



if __name__ == '__main__':
    unittest.main()
