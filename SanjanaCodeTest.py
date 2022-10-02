import unittest
from Assignment_GEDCOM import *

class Test(unittest.TestCase):
    def testOne(self): 
        self.assertEqual(marrigeBeforeDeath("F03"),'No errors in US05')
    def testTwo(self): 
        self.assertEqual(marrigeBeforeDeath("F08"),'Error US05: In family F08 Wife death occurs before marriage.')
    def testThree(self): 
        self.assertEqual(marrigeBeforeDeath("F05"), 'No errors in US05')
    def testFour(self): 
        self.assertEqual(marrigeBeforeDeath("F06"), 'No errors in US05')
    def testFive(self): 
        self.assertNotEqual(marrigeBeforeDeath("F08"), 'No errors in US05')

if __name__ == '__main__':
    unittest.main()