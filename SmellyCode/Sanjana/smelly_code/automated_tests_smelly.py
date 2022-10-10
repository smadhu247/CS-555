import unittest
from smelly_code import *

class Test(unittest.TestCase):
    def test05One(self): 
        self.assertEqual(marrigeBeforeDeath("F03"),'No errors in US05 for family F03')
    def test05Two(self): 
        self.assertEqual(marrigeBeforeDeath("F08"),'No errors in US05 for family F08')
    def test05Three(self): 
        self.assertEqual(marrigeBeforeDeath("F05"), 'Error US05: In family F05 Wife death occurs before marriage.')
    def test05Four(self): 
        self.assertEqual(marrigeBeforeDeath("F06"), 'Error US05: In family F06 Wife death occurs before marriage.')
        
    def test06One(self): 
        self.assertEqual(divorceBeforeDeath("F03"),'No errors in US06 for family F03')
    def test06Two(self): 
        self.assertEqual(divorceBeforeDeath("F08"),'No errors in US06 for family F08')
    def test06Three(self): 
        self.assertEqual(divorceBeforeDeath("F05"), 'Error US06: In family F05 Wife death occurs before divorce.')
    def test06Four(self): 
        self.assertEqual(divorceBeforeDeath("F06"), 'Error US06: In family F06 Wife death occurs before divorce.')


if __name__ == '__main__':
    unittest.main()