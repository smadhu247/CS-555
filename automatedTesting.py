import unittest
from Assignment_GEDCOM import *

class Test(unittest.TestCase):
    # Sprint 1
    # US01
    # US02
    # US03
    def birthBeforeDeathOne(self): 
        self.assertEqual(birthBeforeDeath("I81"),'No errors in US03 for INDI I81.')
    def birthBeforeDeathTwo(self): 
        self.assertEqual(birthBeforeDeath("I82"),'Error USO3: Birth data of Alan /Turning/(I82) occurs after his death date.')
    def birthBeforeDeathThree(self):
        self.assertEqual(birthBeforeDeath("I83"),'No errors in US03 for INDI I83.')
    def birthBeforeDeathFour(self):
        self.assertEqual(birthBeforeDeath("I84"),'No errors in US03 for INDI I84.')
    def birthBeforeDeathFive(self):
        self.assertEqual(birthBeforeDeath("I85"),'Error USO3: Birth data of Jerry /Stin/(I85) occurs after his death date.')
    # US04
    def marrigeBeforeDivorceOne(self):
        self.assertEqual(marrigeBeforeDivorce("F05"),'No errors in US04 for FAM F05')
    def marrigeBeforeDivorceTwo(self):
        self.assertEqual(marrigeBeforeDivorce("F25"),'Error US04: In family F25 divorce but no marrage.')
    def marrigeBeforeDivorceThree(self):
        self.assertEqual(marrigeBeforeDivorce("F111"),'Error US04: In family F111 Divorce occurs before marrage.')
    # US05
    # US06
    # US07
    # US08


if __name__ == '__main__':
    unittest.main()