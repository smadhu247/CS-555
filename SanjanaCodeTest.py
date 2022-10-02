import unittest
from Assignment_GEDCOM import *

class Test(unittest.TestCase):
    def testOne(self): 
        self.assertEqual(marrigeBeforeDeath("F03"),'No errors in US05')
    def testTwo(self): 
        self.assertEqual(divorceBeforeDeath("F03"),'No errors in US06')

if __name__ == '__main__':
    unittest.main()