import unittest
from Assignment_GEDCOM import *

class Test(unittest.TestCase):
    def testOne(self): 
        self.assertEqual(marrigeBeforeDeath("F03"),'No errors in US05 for family F03')
    def testTwo(self): 
        self.assertEqual(marrigeBeforeDeath("F08"),'No errors in US05 for family F08')
    def testThree(self): 
        self.assertEqual(marrigeBeforeDeath("F05"), 'Error US05: In family F05 Wife death occurs before marriage.')
    def testFour(self): 
        self.assertEqual(marrigeBeforeDeath("F06"), 'Error US05: In family F06 Wife death occurs before marriage.')
    def testFive(self): 
        self.assertNotEqual(marrigeBeforeDeath("F08"), 'No errors in US05')

if __name__ == '__main__':
    unittest.main()