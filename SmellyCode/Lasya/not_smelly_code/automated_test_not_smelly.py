import unittest
from not_smelly_code import *

class Test(unittest.TestCase):
    def test05One(self): 
        self.assertEqual(recentBirths("17 OCT 2022"),'US15: Recent Births from 17 OCT 2022 include [\'I21\', \'I22\'].')
    def test05Two(self): 
        self.assertEqual(recentBirths("1 NOV 2002"),'No recent births.')
    def test05Three(self): 
        self.assertEqual(recentBirths("24 FEB 1935"), 'US15: Recent Births from 24 FEB 1935 include [\'I84\', \'I85\'].')
    def test05Four(self): 
        self.assertEqual(recentBirths("10 JAN 2022"), 'No recent births.')
        
    def test06One(self): 
        self.assertEqual(recentDeaths("17 OCT 2022"),'US15: Recent Deaths from 17 OCT 2022 include [\'I23\'].')
    def test06Two(self): 
        self.assertEqual(recentDeaths("26 JAN 1935"),'US15: Recent Deaths from 26 JAN 1935 include [\'I85\'].')
    def test06Three(self): 
        self.assertEqual(recentDeaths("12 OCT 2002"), 'No recent deaths.')
    def test06Four(self): 
        self.assertEqual(recentDeaths("1 JAN 2010"), 'No recent deaths.')


if __name__ == '__main__':
    unittest.main()