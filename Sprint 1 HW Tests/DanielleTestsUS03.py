'''
Danielle Dauphinais
I pledge my honor that I have abided by the Stevens Honor System. DD
M4.B1: Assignment: Homework Assignment 4: Test First
'''

import unittest
from Assignment_GEDCOM import *

class Test(unittest.TestCase):
    def testOne(self): 
        self.assertEqual(birthBeforeDeath("I81"),'No errors in US03 for INDI I81.')
    def testTwo(self): 
        self.assertEqual(birthBeforeDeath("I82"),'Error USO3: Birth data of Alan /Turning/(I82) occurs after his death date.')
    def testThree(self):
        self.assertEqual(birthBeforeDeath("I83"),'No errors in US03 for INDI I83.')
    def testFour(self):
        self.assertEqual(birthBeforeDeath("I84"),'No errors in US03 for INDI I84.')
    def testFive(self):
        self.assertEqual(birthBeforeDeath("I85"),'Error USO3: Birth data of Jerry /Stin/(I85) occurs after his death date.')

if __name__ == '__main__':
    unittest.main()