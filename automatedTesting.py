import unittest
from Assignment_GEDCOM import *

class Test(unittest.TestCase):
    # Sprint 1:
    # US01
    def testdatesBeforeCurrentOne(self): 
        self.assertEqual(datesBeforeCurrent("I01"), "Error USO1: Death date of Nancy /Below/ (15 NOV 2185) occurs after the current date.")
    def testdatesBeforeCurrentTwo(self): 
        self.assertEqual(datesBeforeCurrent("I201"), 'Error USO1: Birth date of John /Below/ (30 DEC 2023) occurs after the current date.')
    def testdatesBeforeCurrentThree(self): 
        self.assertEqual(datesBeforeCurrent("F41"), "Error USO1: Marriage date of F41 (31 JAN 2028) occurs after the current date.")
    def testdatesBeforeCurrentFour(self): 
        self.assertEqual(datesBeforeCurrent("F42"), 'Error USO1: Divorce date of F42 (11 JAN 2089) occurs after the current date.')
    def testdatesBeforeCurrentFive(self):
        self.assertEqual(datesBeforeCurrent("I202"), "Error USO1: Birth date of Jane /Below/ (11 DEC 2098) occurs after the current date.")
    # US02
    # US03
    def testBirthBeforeDeathOne(self): 
        self.assertEqual(birthBeforeDeath("I81"),'No errors in US03 for INDI I81.')
    def testBirthBeforeDeathTwo(self): 
        self.assertEqual(birthBeforeDeath("I82"),'Error USO3: Birth data of Alan /Turning/(I82) occurs after his death date.')
    def testBirthBeforeDeathThree(self):
        self.assertEqual(birthBeforeDeath("I83"),'No errors in US03 for INDI I83.')
    def testBirthBeforeDeathFour(self):
        self.assertEqual(birthBeforeDeath("I84"),'No errors in US03 for INDI I84.')
    def testBirthBeforeDeathFive(self):
        self.assertEqual(birthBeforeDeath("I85"),'Error USO3: Birth data of Jerry /Stin/(I85) occurs after his death date.')
    # US04
    def testMarrigeBeforeDivorceOne(self):
        self.assertEqual(marrigeBeforeDivorce("F05"),'Error US04: In family F05 Divorce occurs before marrage.')
    def testMarrigeBeforeDivorceTwo(self):
        self.assertEqual(marrigeBeforeDivorce("F111"),'Error US04: In family F111 Divorce occurs before marrage.')
    def testMarrigeBeforeDivorceThree(self):
        self.assertEqual(marrigeBeforeDivorce("F06"),'No errors in US04 for FAM F06.')
    # US05
    def testmarrigeBeforeDeathOne(self): 
        self.assertEqual(marrigeBeforeDeath("F03"),'No errors in US05 for family F03')
    def testmarrigeBeforeDeathTwo(self): 
        self.assertEqual(marrigeBeforeDeath("F08"),'No errors in US05 for family F08')
    def testmarrigeBeforeDeathThree(self): 
        self.assertEqual(marrigeBeforeDeath("F05"), 'Error US05: In family F05 Wife death occurs before marriage.')
    def testmarrigeBeforeDeathFour(self): 
        self.assertEqual(marrigeBeforeDeath("F06"), 'Error US05: In family F06 Wife death occurs before marriage.')
    def testmarrigeBeforeDeathFive(self): 
        self.assertNotEqual(marrigeBeforeDeath("F08"), 'No errors in US05')
    # US06
    # US07
    def test_deathLessThan150_1(self): 
        self.assertEqual(deathLessThan150("I01"),'Error US07: With Individual:  I01, Nancy /Below/, Individual is listed as over 150 years old & Death must be within 150 years of birth')
    def test_deathLessThan150_2(self): 
        self.assertEqual(deathLessThan150("I03"),'No Errors with US07')
    
    # Sprint 2:
    # US08
    def test_childDuringMarriage_1(self): 
        self.assertEqual(childDuringMarriage("F03"),'Error US08: Child born out of side of parents marriage Timeline for I03, David /Dauphinais/')
    def test_childDuringMarriage_2(self): 
        self.assertEqual(childDuringMarriage("F05"),'Error US08: Birthday = N/A for I06 Peter /Smith/')
    def test_childDuringMarriage_3(self): 
        self.assertEqual(childDuringMarriage('F06'),'Error US08: Child born out of side of parents marriage Timeline for I08, Danielle /Dauphinais/')
    #US09
    #US10
    #US11
    def test_noBigamy1(self):
        self.assertEqual(noBigamy('I04'),'Error US11: Individual I04 has participated in bigamy')
    def test_noBigamy2(self):
        self.assertEqual(noBigamy('I01'),'I01 has not participated in bigamy')
    #US12
    def test_parentsNotTooOld1(self):
        self.assertEqual(parentsNotTooOld('F08'), 'Error US12: Family F08 has a parent too old.')
    def test_parentsNotTooOld2(self):
        self.assertEqual(parentsNotTooOld('F05'), 'F05 does not have a parent too old.')
    #US13
    #US14
    
    #US15
    def test_fewer15Sibs(self):
        self.assertEqual(fewer15Sibs('F05'), 'No Errors in US15')
    #US16
    def test_matchingMaleLastNames(self):
        fam_ids = ["F03", "F08", "F05", "F06","F09", "F111","F41","F42","F25","F02"]
        indi_ids = ["I01", "I02", "I03", "I04", "I05", "I06", "I07", "I08","I101","I102","I103","I104","I105", "bi00", "I82", "I81", "I83","I84", "I85","I25","I26","I201","I202","I203","I29","I6","I28"]
        self.assertEqual(matchingMaleLastNames(indi_ids,fam_ids), ['US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name'])





if __name__ == '__main__':
    unittest.main()
