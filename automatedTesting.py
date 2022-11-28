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
        self.assertEqual(birthBeforeDeath("I81"),'Error USO3: Birth data of Kennith /Joy/(I81) occurs after his death date.')
    def testBirthBeforeDeathTwo(self): 
        self.assertEqual(birthBeforeDeath("I82"),'Error USO3: Birth data of Alan /Turning/(I82) occurs after his death date.')
    def testBirthBeforeDeathThree(self):
        self.assertEqual(birthBeforeDeath("I83"),'Error USO3: Birth data of Alex /Wazi/(I83) occurs after his death date.')
    def testBirthBeforeDeathFour(self):
        self.assertEqual(birthBeforeDeath("I84"),'Error USO3: Birth data of Harry /Dauphinais/(I84) occurs after his death date.')
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
    def testdivorceeforeDeathOne(self): 
        self.assertEqual(divorceBeforeDeath("F03"),'No errors in US06 for family F03') 
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
    def test_birthBeforeParentsDeath1(self):
        self.assertEqual(birthBeforeParentsDeath('bi00'), 'Error US09: No information about the family bi00 belongs to.')
    def test_birthBeforeParentsDeath2(self):
        self.assertEqual(birthBeforeParentsDeath('I06'), 'Error US09: No birthday recorded for I06')
    #US10
    def test_marriageAfter141(self):
        self.assertEqual(marriageAfter14('I05'), 'Error US10: Spouse of individual I05, with ID I04 is younger than 14 years old and married.')
    def test_marriageAfter142(self):
        self.assertEqual(marriageAfter14('I02'), 'Error US10: Individual I02 is younger than 14 years old and married.')
    def test_marriageAfter143(self):
        self.assertEqual(marriageAfter14('I203'), 'Individual I203 and all of his/her spouses were at least 14 years old when married')
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
    def test_siblingSpacingOne(self):
        self.assertEqual(siblingSpacing('F08'), 'US13: Family F08 does not contain a family with siblings.')
    def test_siblingSpacingTwo(self):
        self.assertEqual(siblingSpacing('F05'), 'US13: Family F05 does not contain a family with siblings.')
    #US14
    def test_multipleBirthsOne(self):
            self.assertEqual(multipleBirths('F08'), 'US14: Family F08 does not contain a family with siblings.')
    def test_multipleBirthsTwp(self):
            self.assertEqual(multipleBirths('F05'), 'US14: Family F05 does not contain a family with siblings.')
    #US15
    def test_fewer15Sibs(self):
        self.assertEqual(fewer15Sibs('F05'), 'No Errors in US15')
    #US16
    def test_matchingMaleLastNames(self):
        fam_ids = ["F03", "F08", "F05", "F06","F09", "F111","F41","F42","F25","F02"]
        indi_ids = ["I01", "I02", "I03", "I04", "I05", "I06", "I07", "I08","I101","I102","I103","I104","I105", "bi00", "I82", "I81", "I83","I84", "I85","I25","I26","I201","I202","I203","I29","I6","I28"]
        self.assertEqual(matchingMaleLastNames(indi_ids,fam_ids), ['US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name', 'US16: Error, All of the men in this family F02 do not have the same last name'])
    
    # Sprint 3:
    #US17
    def test_noMarriageDescendants1(self):
        self.assertEqual(noMarriageDescendant('I58'), 'Error US17: Individual I58s spouse is also their descendent')
    def test_noMarriageDescendants2(self):
        self.assertEqual(noMarriageDescendant('I204'), 'US17: Individual I204 has no descendants. No errors in US17.')
    def test_noMarriageDescendants3(self):
        self.assertEqual(noMarriageDescendant('I003'), 'No errors in US17')
    #US18
    def test_siblingsNotMarried1(self):
        self.assertEqual(siblingsNotMarried('I301'), 'Error US18: Individual I301 and spouse I302 are siblings.')
    def test_siblingsNotMarried2(self):
        self.assertEqual(siblingsNotMarried('I58'), 'No information given about I58s siblings.')
    def test_siblingsNotMarried3(self):
        self.assertEqual(siblingsNotMarried('I10'), 'No errors in US18')
    #US19
    def test_1FirstCousinsChouldNotMarry(self):
        self.assertEqual(FirstCousinsChouldNotMarry('I0010'), 'Error US19: individual I0010 is married to a cousin.')
    def test_2FirstCousinsChouldNotMarry(self):
        self.assertEqual(FirstCousinsChouldNotMarry('I08'), 'I08 is not married to a cousin.')
    #US20
    def test_1AuntsAndUncles(self):
        self.assertEqual(AuntsAndUncles('I005'), 'Error US20: individual I005 is married to a niece or nephew.')
    def test_2AuntsAndUncles(self):
        self.assertEqual(AuntsAndUncles('I08'), 'I08 is not married to a niece or nephew.')
    #US21
    def testcorrectGenderRole(self):
        self.assertEqual(correctGenderRole('F51'), 'Error US21: Husband I59 in family F51 is not male.')
    #US22
    def testuniqueIDsFams(self):
        self.assertEqual(uniqueIDsFams('F25'), 'Error US22: Family ID F25 is not unqiue.')
    def testuniqueIDsIndis(self):
        self.assertEqual(uniqueIDsIndis('I28'), 'Error US22: Individual ID I28 is not unqiue.')
    #US23
    def testUniqueIndiv(self):
        self.assertEqual(uniqueIndiv('I101'), 'ERROR US23: Individual:  Jessica /Dauphinais/ exists multiple times within the file .')
    def testUniqueIndiv2(self):
        self.assertEqual(uniqueIndiv('I08'), 'US23: no error found')
    #US24
    def testUniqueFamily(self):
        self.assertEqual(uniqueFamily('I08'), 'Error US24 Fam ID not in file')
    def testUniqueFamily1(self):
        self.assertEqual(uniqueFamily('F08'), 'US24: no error found')
    
    # Sprint 4
    #US25
    def test1_uniqueNames(self):
        self.assertEqual(uniqueNames('F06'),'Error US25: There is more than one child in the family F06 with the name Jessica /Dauphinais/ and the birthday 10 APR 2003.')
    def test2_uniqueNames(self):
        self.assertEqual(uniqueNames('F101'), 'There is no family with ID F101.')
    #US33
    def testListOrphans(self):
        self.assertEqual(listOrphans(), "US33: List of orphans ['I60'].")
    #US27
    def test1_individualAges(self):
        self.assertEqual(individualAges('I03'),'US27: Individul David /Dauphinais/ (I03) has the age of 60.')
    def test2_individualAges(self):
        self.assertEqual(individualAges('I0109'), "US27: I0109 not found.")
    #US28
    def test1_orderSiblingsByAge(self):
        self.assertEqual(orderSiblingsByAge('F42'), "US28: Family F42 has not children.")
    def test2_orderSiblingsByAge(self):
        self.assertEqual(orderSiblingsByAge('F11'), "US28: Family F11 not found.")
    def test3_orderSiblingsByAge(self):
        self.assertEqual(orderSiblingsByAge('F06'), "US28: Family F06 has children ['I07', 'I08', 'I105', 'I104', 'I103', 'I102', 'I101'] listed oldest to youngest.")
    #US29
    def testlistDeceased(self):
        self.assertEqual(listDeceased(), "US29: List of deceased members: I02, I04, I81, I82, I83, I84, I85, I58, I59")
    #US30
    def testlistLivingMarried(self):
        self.assertEqual(listLivingMarried(), "US30: List of living married: I01")
    #US31
    def testLivingSingle(self):
        self.assertEqual(listLivingSingle(),['Jim /Halpert/'])
    #US32
    def testListMulBirth(self):
        self.assertEqual(listMulBirth(modified_file),['Pam /Halpert/'])
  


if __name__ == '__main__':
    unittest.main()
