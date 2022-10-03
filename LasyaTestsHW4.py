import unittest
from Assignment_GEDCOM import *

class Test(unittest.TestCase):
    def testOne(self): 
        self.assertEqual(datesBeforeCurrent("I01"), "Error USO1: Death date of Nancy /Below/ (15 NOV 2185) occurs after the current date.")
    def testTwo(self): 
        self.assertEqual(datesBeforeCurrent("I201"), 'Error USO1: Birth date of John /Below/ (30 DEC 2023) occurs after the current date.')
    def testThree(self): 
        self.assertEqual(datesBeforeCurrent("F41"), "Error USO1: Marriage date of F41 (31 JAN 2028) occurs after the current date.")
    def testFour(self): 
        self.assertEqual(datesBeforeCurrent("F42"), 'Error USO1: Divorce date of F42 (11 JAN 2089) occurs after the current date.')
    def testFive(self):
        self.assertEqual(datesBeforeCurrent("I202"), "Error USO1: Birth date of Jane /Below/ (11 DEC 2098) occurs after the current date.")

if __name__ == '__main__':
    unittest.main()