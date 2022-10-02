#My Tests Will Go here 
import unittest
from Assignment_GEDCOM import *

class Test(unittest.TestCase):
    def test_deathLessThan150_1(self): 
        self.assertEqual(deathLessThan150("I01"),'Error US07: With Individual:  I01, Nancy /Below/, Individual is listed as over 150 years old & Death must be within 150 years of birth')
    def test_deathLessThan150_2(self): 
        self.assertEqual(childDuringMarriage("F03"),'No Errors with US07')
    def test_childDuringMarriage_1(self): 
        self.assertEqual(deathLessThan150("F03"),'Error US08: Child born out of side of parents marriage Timeline for I03, David /Dauphinais/')
    def test_childDuringMarriage_2(self): 
        self.assertEqual(deathLessThan150("F05"),'Error US08: Child born out of side of parents marriage Timeline for I06, Peter /Smith/')
    def test_childDuringMarriage_3(self): 
        self.assertEqual(deathLessThan150("F06"),'Error US08: Child born out of side of parents marriage Timeline for I08, Danielle /Dauphinais/')
if __name__ == '__main__':
    unittest.main()
