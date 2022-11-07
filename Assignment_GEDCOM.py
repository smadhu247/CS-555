from mailbox import ExternalClashError
from typing import final
from unittest.result import failfast
from prettytable import PrettyTable
from datetime import *
from dateutil.relativedelta import *

file = open('test.ged', 'r')
individuals = PrettyTable()
individuals.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

families = PrettyTable()
families.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

acceptable_tags_0 = ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE']
acceptable_tags_1 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
acceptable_tags_2 = ['DATE']


#Code to essentially take the entire input file, and make it into a list of lists. Each list
#is each line. Each list's zero index is the level. First index is tag. Second index is the 
#notes/extra information. Third index is a boolean indicating if this line was level 0. Fourth
#index indicates if tag FAMC or FAMS was seen.

modified_file = []
for line in file:
    words = line.split()
    
    if (words[0] == '0'):

        sawZero = 0
        if (words[1] in acceptable_tags_0):
            if (words[1] == 'HEAD' or words[1] == 'TRLR' or words[1] == 'NOTE'):
                temp = []
                level = words[0]
                tag = words[1]
                words.pop(0)
                words.pop(0)
                if (len(words) == 0):
                    temp.append(level)
                    temp.append(tag)
                    temp.append(' ')
                    temp.append(True)
                    temp.append('not seen')
                    modified_file.append(temp)
                else:
                    sent = " ".join(words)
                    temp.append(level)
                    temp.append(tag)
                    temp.append(sent)
                    temp.append(True)
                    temp.append('not seen')
                    modified_file.append(temp)

        elif (words[2] in acceptable_tags_0):
            if (words[2] == 'INDI' or words[2] == 'FAM'):
                temp = []
                temp.append(words[0].strip())
                temp.append(words[2].strip())
                temp.append(words[1].strip())
                temp.append(True)
                temp.append('not seen')
                modified_file.append(temp)
            else:
                temp = []
                level = words[0]
                tag = words[2]
                words.pop(0)
                words.pop(1)
                if (len(words) == 0):
                    temp.append(level)
                    temp.append(tag)
                    temp.append(' ')
                    temp.append(True)
                    temp.append('not seen')
                    modified_file.append(temp)
                else:
                    sent = " ".join(words)
                    temp.append(level)
                    temp.append(tag)
                    temp.append(sent)
                    temp.append(True)
                    temp.append('not seen')
                    modified_file.append(temp)
        else:
            temp = []
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if (len(words) == 0):
                temp.append(level)
                temp.append(tag)
                temp.append(' ')
                temp.append(True)
                temp.append('not seen')
                modified_file.append(temp)            
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(True)
                temp.append('not seen')
                modified_file.append(temp)
    
    elif (words[0] == '1'):
        if (words[1] in acceptable_tags_1):
            temp = []
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if (tag == 'FAMC'):
                if(len(words) == 0):
                    temp.append(level)
                    temp.append(tag)
                    temp.append(' ')
                    temp.append(False)
                    temp.append('famc')
                    modified_file.append(temp)
                else:
                    sent = " ".join(words)
                    temp.append(level)
                    temp.append(tag)
                    temp.append(sent)
                    temp.append(False)
                    temp.append('famc')
                    modified_file.append(temp)
            elif (tag == 'FAMS'):
                if(len(words) == 0):
                    temp.append(level)
                    temp.append(tag)
                    temp.append(' ')
                    temp.append(False)
                    temp.append('fams')
                    modified_file.append(temp)
                else:
                    sent = " ".join(words)
                    temp.append(level)
                    temp.append(tag)
                    temp.append(sent)
                    temp.append(False)
                    temp.append('fams')
                    modified_file.append(temp)
            else:
                if(len(words) == 0):
                    temp.append(level)
                    temp.append(tag)
                    temp.append(' ')
                    temp.append(False)
                    temp.append('not seen')
                    modified_file.append(temp)
                else:
                    sent = " ".join(words)
                    temp.append(level)
                    temp.append(tag)
                    temp.append(sent)
                    temp.append(False)
                    temp.append('not seen')
                    modified_file.append(temp)
        else:
            temp = []
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if(len(words) == 0):
                temp.append(level)
                temp.append(tag)
                temp.append(' ')
                temp.append(False)
                temp.append('not seen')
                modified_file.append(temp)
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(False)
                temp.append('not seen')
                modified_file.append(temp)

    elif (words[0] == '2'):
        if (words[1] in acceptable_tags_2):
            temp = []
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if(len(words) == 0):
                temp.append(level)
                temp.append(tag)
                temp.append(' ')
                temp.append(False)
                temp.append('not seen')
                modified_file.append(temp)
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(False)
                temp.append('not seen')
                modified_file.append(temp)
        else:
            temp = []
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if(len(words) == 0):
                temp.append(level)
                temp.append(tag)
                temp.append(' ')
                temp.append(False)
                temp.append('not seen')
                modified_file.append(temp)
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(False)
                temp.append('not seen')
                modified_file.append(temp)

#print (modified_file)


indi_list = []
indi = []
i = 0
famc = 0
fams = 0

months_short = [' ','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
months_long = [' ','january', 'february', 'march', 'april', 'may', 'jun', 'july', 'august', 'september', 'october', 'november', 'december']

for i in range(len(modified_file)):
    birthday = date.today()
    if (modified_file[i][3] == True):
        if (modified_file[i][1] == 'INDI'):
            indi = ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', True, 'N/A', 'N/A', 'N/A']
            indi[0] = modified_file[i][2]
        else:
            continue
    
    elif(modified_file[i][0] == '1'):
        if (modified_file[i][1] == 'NAME'):
            indi[1] = modified_file[i][2]

        if (modified_file[i][1] == 'SEX'):
            indi[2] = modified_file[i][2]

        if (modified_file[i][1] == 'BIRT'):
            if (modified_file[i+1][1] == 'DATE'):
                indi[3] = modified_file[i+1][2]
                today = date.today()
                birthday = datetime.strptime(modified_file[i+1][2], '%d %b %Y').date()
                age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
                indi[4] = age

        if (modified_file[i][1] == 'DEAT'):
            indi[5] = False
            if (modified_file[i+1][1] == 'DATE'):
                indi[6] = modified_file[i+1][2]
                death = datetime.strptime(modified_file[i+1][2], '%d %b %Y').date()
                death_age = death.year - birthday.year - ((death.month, death.day) < (birthday.month, birthday.day))
                indi[4] = death_age

        if (modified_file[i][1] == 'FAMC'):
            famc_list = []
            famc = i
            
            if (modified_file[i][4] == 'famc'):
                famc_list.append(modified_file[i][2])
                modified_file[i][4] = 'famc seen'
                
                # while(modified_file[famc][1] == 'FAMC' and modified_file[famc+1][1] == 'FAMC'):
                #     famc_list.append(modified_file[famc+1][2])
                #     modified_file[famc+1][4] = 'famc seen'
                #     famc = famc+1
            else:
                continue
                
            indi[7] = famc_list

        if (modified_file[i][1] == 'FAMS'):
            fams_list = []
            fams = i
            
            if (modified_file[i][4] == 'fams'):
                fams_list.append(modified_file[i][2])
                modified_file[i][4] = 'fams seen'
                
                # while(modified_file[fams][1] == 'FAMS' and modified_file[fams+1][1] == 'FAMS'):
                #     fams_list.append(modified_file[fams+1][2])
                #     modified_file[fams+1][4] = 'fams seen'
                #     fams = fams+1
            else:
                continue
                
            indi[8] = fams_list     
    # fixed smelly code here
    if(indi in indi_list):
        continue
    else:     
        indi_list.append(indi)        

final_indi = indi_list

individuals.add_rows(
    final_indi
)


print(individuals)

j = 1
for i in range(len(modified_file)):  
    if (modified_file[i][0] == '0' and modified_file[i][1] == "FAM"):
        j = j + 1     
    if (modified_file[i][0] == '0' and modified_file[i][1] == "INDI"):
        j = j + 1 
    modified_file[i].append(j)

j = 1
clusters_list = []
cluster = []
for i in range(len(modified_file)):   
    if modified_file[i][-1] == j:
        cluster.append(modified_file[i])
    else:
        clusters_list.append(cluster)
        cluster = []
        cluster.append(modified_file[i])
        j = j + 1
clusters_list.append(cluster)

siblings = {}
# created a family list to easily access information about each family with out having to go through cluster_list
familyList = []
for i in range(len(clusters_list)):
    if (clusters_list[i][0][1] == "FAM"):
        children = set()
        married = "N/A"
        divorced = "N/A"
        wife_id = "N/A"
        husband_id = "N/A"
        husband_name = "N/A"
        wife_name = "N/A"
        id = clusters_list[i][0][2]
        for j in range(len(clusters_list[i])):
            if (clusters_list[i][j][1] == "MARR"):
                married = clusters_list[i][j+1][2]
            if (clusters_list[i][j][1] == "DIV"):
                divorced = clusters_list[i][j+1][2]
            if(clusters_list[i][j][1] == "HUSB"):
                husband_id = clusters_list[i][j][2]
            if(clusters_list[i][j][1] == "WIFE"):
                wife_id = clusters_list[i][j][2]
            if(clusters_list[i][j][1] == "CHIL"):
                children.add(clusters_list[i][j][2])
        if (len(children) == 0):
            children = {}
        wife_name = ""
        husband_name = ""
        for i in range(len(modified_file)):
            if modified_file[i][0] == "0" and  modified_file[i][1] == "INDI" and modified_file[i][2] == husband_id:
                if (modified_file[i+1][1] == "NAME"):
                    husband_name = modified_file[i+1][2]
            if modified_file[i][0] == "0" and  modified_file[i][1] == "INDI" and modified_file[i][2] == wife_id:
                if (modified_file[i+1][1] == "NAME"):
                    wife_name = modified_file[i+1][2]
        families.add_row([id, married, divorced, husband_id, husband_name, wife_id, wife_name, children])
        familyList.append([id, married, divorced, husband_id, husband_name, wife_id, wife_name, children])
        siblings[id] = children


print(families)  


'''
US01 - Sprint 1
Story Name: Dates before current date
Description: Dates (birth, marriage, divorce, death) should not be after the current date 
'''

def datesBeforeCurrent(ID):
     splitLetters = list(ID)
     if (splitLetters[0] == 'I'):
         for i in range(len(final_indi)):
             if (ID == final_indi[i][0]):
                 #birthday
                 if (final_indi[i][3] != 'N/A'):
                     birthday = datetime.strptime(final_indi[i][3], '%d %b %Y').date()
                     if (today < birthday):
                         return "Error USO1: Birth date of " + final_indi[i][1]+ " (" + final_indi[i][3] +") occurs after the current date."
                 #death
                 if (final_indi[i][6] != 'N/A'):
                     death = datetime.strptime(final_indi[i][6], '%d %b %Y').date()
                     if (today < death):
                         return "Error USO1: Death date of " + final_indi[i][1]+ " (" + final_indi[i][6] +") occurs after the current date."
     elif (splitLetters[0] == 'F'):
         for i in range(len(clusters_list)):
             if (clusters_list[i][0][1] == "FAM"):
                 id = clusters_list[i][0][2]
                 if (id == ID):
                     marriage = 0
                     divorce = 0
                     for j in range(len(clusters_list[i])):
                         #marriage
                         if (clusters_list[i][j][1] == "MARR"):
                             marriage = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()
                             if (today < marriage):
                                 return "Error USO1: Marriage date of " + id + " (" + clusters_list[i][j+1][2] +") occurs after the current date."
                         #divorce
                         if (clusters_list[i][j][1] == "DIV"):
                             divorce = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()
                             if (today < divorce):
                                 return "Error USO1: Divorce date of " + id + " (" + clusters_list[i][j+1][2] +") occurs after the current date."
     else:
         return "No errors in US01"

'''
US02 - Sprint 1
Story Name: Birth before marriage
Description: Birth should occur before marriage of an individual
'''

def birthBeforeMarr(INDI_ID):
    marriedPeople = []
    for i in range (len(final_indi)):
        person = []
        if (INDI_ID == final_indi[i][0]):
            if (final_indi[i][8] != 'N/A'):
                person.append(final_indi[i][0])
                person.append(final_indi[i][1])
                person.append(final_indi[i][3])
                person.append(final_indi[i][8])
                marriedPeople.append(person)

    for i in range(len(marriedPeople)):
        if (marriedPeople[i][2] != 'N/A'):
            birthday = datetime.strptime(marriedPeople[i][2], '%d %b %Y').date()
            if (len(marriedPeople[i][3]) == 1):
                for j in range(len(clusters_list)):
                    if (clusters_list[j][0][1] == 'FAM'):
                        id = clusters_list[j][0][2]
                        if (id == marriedPeople[i][3][0]):
                            for k in range (len(clusters_list[j])):
                                if (clusters_list[j][k][1] == 'MARR'):
                                    marriage = datetime.strptime(clusters_list[j][k+1][2], '%d %b %Y').date()
                                    if (birthday > marriage):
                                        return "Error USO2: Marriage date of " + id + " (" + clusters_list[j][k+1][2] +") occurs before the birth date of " + marriedPeople[i][1] + " (" + marriedPeople[i][2] + ")."
            if (len(marriedPeople[i][3]) > 1):
                for j in range (len(marriedPeople[i][3])):
                    indiMarrId = marriedPeople[i][3][j]
                    for k in range(len(clusters_list)):
                        if (clusters_list[k][0][1] == 'FAM'):
                            id = clusters_list[k][0][2]
                            if (id == indiMarrId):
                                for l in range(len(clusters_list[k])):
                                    if (clusters_list[k][l][1] == 'MARR'):
                                        marriage = datetime.strptime(clusters_list[k][l+1][2], '%d %b %Y').date()
                                        if (birthday > marriage):
                                            return "Error USO2: Marriage date of " + id + " (" + clusters_list[k][l+1][2] +") occurs before the birth date of " + marriedPeople[i][1] + " (" + marriedPeople[i][2] + ")."
    return "No errors in US02"
                                      
'''
US03 - Sprint 1
Story Name: Birth before death
Description: Birth should occur before death of an individual
'''
def birthBeforeDeath(INDI_ID):
    for i in range(len(final_indi)):
        if(INDI_ID == final_indi[i][0]):
            if (final_indi[i][4] != "N/A"):
                if (final_indi[i][4] < 0):
                    return "Error USO3: Birth data of " + final_indi[i][1]+ "(" + final_indi[i][0] +")" " occurs after his death date."
    return "No errors in US03 for INDI "+INDI_ID+ "."

'''
US04 - Sprint 1
Story Name: Marriage before divorce
Description: Marriage should occur before divorce of spouses, and divorce can only occur after marriage
'''
def marrigeBeforeDivorce(FAM_ID):
    for i in range(len(clusters_list)):
        if (clusters_list[i][0][1] == "FAM"):
            id = clusters_list[i][0][2]
            if(FAM_ID == id):
                MARR = date.today()
                DIV = date.today()
                for j in range(len(clusters_list[i])):
                    if (clusters_list[i][j][1] == "MARR"):
                        MARR = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()
                    if (clusters_list[i][j][1] == "DIV"):
                        DIV = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()
                    if (DIV != 'N/A' and DIV != date.today()):
                        if (DIV < MARR):
                            return "Error US04: In family " + id + " Divorce occurs before marrage."
                        else:
                            return "No errors in US04 for FAM "+FAM_ID+ "."
                return "No errors in US04 for FAM "+FAM_ID+ "."
    return FAM_ID +" is not found"

def checkBeforeDeath(FAM_ID, user_story_num, action, indicator):
    for i in range(len(clusters_list)):
            date = 0
            husb_date = "N/A"
            wife_date = "N/A"
            if (clusters_list[i][0][2].strip() == FAM_ID.strip() and clusters_list[i][0][1] == "FAM"):
                id = clusters_list[i][0][2]
                husb_id = ""
                wife_id = ""
                for j in range(len(clusters_list[i])):
                    if (clusters_list[i][j][1] == indicator):
                        date = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()

                    if (clusters_list[i][j][1] == "HUSB"):
                        husb_id = clusters_list[i][j][2]
                        for k in range(len(clusters_list)):
                            if (clusters_list[k][0][1] == "INDI" and str(clusters_list[k][0][2]) == str(husb_id)):
                                for m in range(len(clusters_list[k])):
                                    if (clusters_list[k][m][1] == "DEAT"):
                                        husb_date = datetime.strptime(clusters_list[k][m+1][2], '%d %b %Y').date()

                    if (clusters_list[i][j][1] == "WIFE"):
                        wife_id = clusters_list[i][j][2]
                        for k in range(len(clusters_list)):
                            if (clusters_list[k][0][1] == "INDI" and str(clusters_list[k][0][2]) == str(wife_id)):
                                for m in range(len(clusters_list[k])):
                                    if (clusters_list[k][m][1] == "DEAT"):
                                        wife_date = datetime.strptime(clusters_list[k][m+1][2], '%d %b %Y').date()

                if (husb_date != "N/A" and date != 0 and husb_date < date):
                    return "Error " + user_story_num + ": In family " + id + " Husband death occurs before " + action + "."
                if (wife_date != "N/A" and date != 0 and wife_date < date):
                    return "Error " + user_story_num + ": In family " + id + " Wife death occurs before " + action + "."
    return "No errors in " + user_story_num + " for family " + FAM_ID

'''
US05 - Sprint 1
Story Name: Marriage before death
Description: Marriage should occur before death of either spouse
'''
def marrigeBeforeDeath(FAM_ID):
    return checkBeforeDeath(FAM_ID, "US05", "marriage", "MARR")

'''
US06 - Sprint 1
Story Name: Divorce before death
Description: Divorce can only occur before death of both spouses
'''
def divorceBeforeDeath(FAM_ID):
    return checkBeforeDeath(FAM_ID, "US06", "divorce", "DIV")

'''
US07 - Sprint 1
Story Name: Less then 150 years old
Description: Death should be less than 150 years after birth for dead people, and current date should be less than 150 years after birth for all living people 
'''
def deathLessThan150(indID):
    for i in range(len(final_indi)):
        if (indID==final_indi[i][0]):
            if (final_indi[i][4] != "N/A"):
                if (final_indi[i][4])>= 150:
                    if (final_indi[i][6] != "N/A"):
                        return "Error US07: With Individual:  "+ str(final_indi[i][0])+", "+ str(final_indi[i][1])+", Individual is listed as over 150 years old & Death must be within 150 years of birth"
                    else: 
                        return "Error US07: With Individual:  "+ str(final_indi[i][0])+", "+ str(final_indi[i][1])+", Death is at least 150 years after birth"
                else:
                    return "No Errors with US07"
    return 'ID Never Found '        
       
'''
US08 - Sprint 1
Story Name: Birth before marriage of parents
Description: Children should be born after marriage of parents (and not more than 9 months after their divorce)
'''
def childDuringMarriage(famID):
    #go through family chart,
        # take marrige & divorce date
        # for each child, grab their birthdate, 
                #if birthdate is not between the range of marriage and divorce +9 months 
                    #Error
            
    parAndKids=[]
    count = 0
    for i in range(len(clusters_list)):
        if (clusters_list[i][0][2] == famID and clusters_list[i][0][1] == "FAM"):
            parAndKids.append([clusters_list[i][0][2]])
            count= count+1
            marrDate = 0
            divDate = 0
            
            for j in range(len(clusters_list[i])):
                if (clusters_list[i][j][1] == "MARR"):
                    marrDate = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()
                    parAndKids[count-1].append(marrDate)
                if (clusters_list[i][j][1] == "DIV"):
                    divDate = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()
                    parAndKids[count-1].insert(2,("DIV"))
                    parAndKids[count-1].insert(3,(divDate))
                if (clusters_list[i][j][1] == "CHIL"):
                    parAndKids[count-1].append(clusters_list[i][j][2])
    for k in range(len(final_indi)):
        for l in range(len(parAndKids)):
            divDate=0
            marrDate=0
            flag=False 
            for m in range (len(parAndKids[l])):
        
                marrDate=parAndKids[l][1]

                if "DIV" in parAndKids[l]:
                    divDate = parAndKids[l][parAndKids[l].index("DIV")+1] 
        
                if str(final_indi[k][0]) == str(parAndKids[l][m]) :
                    if final_indi[k][3]!='N/A':
                        birthDate = datetime.strptime(final_indi[k][3], '%d %b %Y').date()
                        parAndKids[l].insert(parAndKids[l].index(final_indi[k][0])+1,birthDate)


                        if (birthDate < marrDate or ( divDate!=0 and birthDate > divDate))and flag==False:
                            flag=True 
                            return("Error US08: Child born out of side of parents marriage Timeline for "+ str(final_indi[k][0])+", "+ str(final_indi[k][1]))
                    else:
                        return 'Error US08: Birthday = N/A for '+final_indi[k][0]+' '+final_indi[k][1]
    return "No errors in US08"

'''
US09 - Sprint 2
Story Name: Birth before death of parents
Description: Child should be born before death of mother and before 9 months after death of father
'''
def birthBeforeParentsDeath(indID):
    mothersDeathDate = ""
    fathersDeathDate = ""
    child_birthday = ""
    wifeID = ""  
    husbID = ""
    nineMonthsAfterDadDeath = ""
    
    for i in range(len(final_indi)):
        if (final_indi[i][0] == indID):
            if (final_indi[i][7] != 'N/A'):
                child_birthday_str = final_indi[i][3]
                if (child_birthday_str != 'N/A'):
                    child_birthday = datetime.strptime(child_birthday_str, '%d %b %Y').date()
                    
                    family = final_indi[i][7]
                    
                    for j in range(len(family)):
                        child_fam = family[j]

                        for k in range(len(familyList)):
                            if (familyList[k][0] == child_fam):
                                wifeID = familyList[k][5]
                                husbID = familyList[k][3]
                else:
                    return 'Error US09: No birthday recorded for ' + indID
            else:
                return 'Error US09: No information about the family ' + indID + ' belongs to.'
    
    for wife in range(len(final_indi)):
        if (final_indi[wife][0] == wifeID):
            if (final_indi[wife][5] == False):
                mothersDeathDate_str = final_indi[wife][6]
                mothersDeathDate = datetime.strptime(mothersDeathDate_str, '%d %b %Y').date()
            else:
                mothersDeathDate = ''
    
    for husb in range(len(final_indi)):
        if (final_indi[husb][0] == husbID):
            if (final_indi[husb][5] == False):
                fathersDeathDate_str = final_indi[husb][6]
                fathersDeathDate = datetime.strptime(fathersDeathDate_str, '%d %b %Y').date()
                nineMonthsAfterDadDeath = fathersDeathDate + relativedelta(months=+9)
            else:
                fathersDeathDate = ''
        
    
    if (fathersDeathDate != '' and mothersDeathDate != ''):
        if ((child_birthday > mothersDeathDate) and (child_birthday < nineMonthsAfterDadDeath)):
            return 'Error US09: Child ' + indID + ' was born after death of mother and after 9 months after death of father'

    return 'No errors in US09'
    
'''
US10 - Sprint 2
Story Name: Marriage After 14
Description: Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
'''
def marriageAfter14(indID):
    spouseID = ""
    for i in range(len(final_indi)):
        if (final_indi[i][0] == indID):
            if (final_indi[i][8] != 'N/A'):
                if (final_indi[i][4] != 'N/A'):
                    if (final_indi[i][4] < 14):
                        return 'Error US10: Individual ' + indID + ' is younger than 14 years old and married.'
                    else:
                        spouses = final_indi[i][8]

                        for l in range(len(spouses)):
                            spouse_fam = spouses[l]

                            for j in range(len(familyList)):
                                if (familyList[j][0] == spouse_fam):
                                    if (familyList[j][3] == indID):
                                        spouseID = familyList[j][5]
                                    else:
                                        spouseID = familyList[j][3]
                            
                            for k in range(len(final_indi)):
                                if (final_indi[k][0] == spouseID):
                                    if (final_indi[k][4] < 14):
                                        return 'Error US10: Spouse of individual ' + indID + ', with ID ' + spouseID + ' is younger than 14 years old and married.'
    return 'Individual ' + indID + ' and all of his/her spouses were at least 14 years old when married'

                        


'''
US11 - Sprint 2
Story Name: No bigamy
Description: Marriage should not occur during marriage to another spouse
'''
def noBigamy(indID):
    count = 0
    dates = []
    for i in range(len(familyList)):
        if(indID in familyList[i]):
            count=count+1
            # need to figure out how to deal with widows
            deathDateH=0
            deathDateW=0
            endDate = familyList[i][2]
            for j in range(len(final_indi)):
                #checking husband death date
                if (final_indi[j][0]==familyList[i][3] and final_indi[j][5]==False):
                    deathDateH = final_indi[j][6]
                    if (familyList[i][2] == 'N/A'):
                        endDate= deathDateH
                #checking wife death date
                if(final_indi[j][0]==familyList[i][5] and final_indi[j][5]==False):
                    deathDateW = final_indi[j][6]
                    if (familyList[i][2] == 'N/A' or (endDate==deathDateH and endDate!=0 and deathDateW<endDate)):
                        endDate= deathDateW
            dates.append([familyList[i][1],endDate])
    if (count>1):
        for i in range(len(dates)-1):
            if(dates[i][1]=='N/A' or dates[i][1]>dates[i+1][0]):
                return 'Error US11: Individual '+ str(indID) + ' has participated in bigamy'
    return str(indID) + " has not participated in bigamy"


'''
US12 - Sprint 2
Story Name: Parents not too old
Description: Mother should be less than 60 years older than her children and father should be less 
than 80 years older than his children
'''
def parentsNotTooOld(famID):
    for i in range(len(familyList)):
        if (familyList[i][0] == famID):
            motherAge = 0
            fatherAge = 0
            for j in range(len(final_indi)):
                #getting mothers age
                if (final_indi[j][0]==familyList[i][5]):
                    motherAge = final_indi[j][4]
                #getting fathers age
                if (final_indi[j][0]==familyList[i][3]):
                    fatherAge = final_indi[j][4]
            #getting kids ages
            for j in range(len(final_indi)):
                if (final_indi[j][0] in familyList[i][7]):
                    if((final_indi[j][4] != "N/A") and (motherAge-final_indi[j][4]>60 or fatherAge-final_indi[j][4]>80)):
                        return ('Error US12: Family '+ str(famID) + ' has a parent too old.')
    return (str(famID) + ' does not have a parent too old.')
                    


'''
US13 - Sprint 2
Story Name: Siblings spacing
Description: Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
(twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''


def siblingSpacing(famID):
    birthdays = []
    issues = []
    for key, value in siblings.items():
        if (key == famID and len(value) > 1):
            children = list(value)
            for child in range(len(children)):
                for i in range(len(clusters_list)):
                    if (clusters_list[i][0][1] == "INDI" and clusters_list[i][0][2] == children[child]):
                        for j in range(len(clusters_list[i])):
                            if(clusters_list[i][j][1]) == "BIRT":
                                birthdays.append(datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date())
    if(len(birthdays) > 0):
        for i in range(len(birthdays)):
            for j in range(len(birthdays)):
                if (abs((birthdays[i].year - birthdays[j].year) * 12 + birthdays[i].month - birthdays[j].month) < 8 and birthdays[i].day - birthdays[j].day < 2 and birthdays[i] != birthdays[j]):
                    issues.append([birthdays[i], birthdays[j]])
        if len(issues) > 0:
            return "Error US13: Siblings are not properly spaced."
        else:
            return "US13: Siblings in Family " + famID + " are properly spaced."
        
    else:
        return "US13: Family " + famID + " does not contain a family with siblings."   

'''
US14 - Sprint 2
Story Name: Multiple births <= 5
Description: No more than five siblings should be born at the same time
'''

def multipleBirths(famID):
    birthdays = []
    for key, value in siblings.items():
        if (key == famID and len(value) > 1):
            children = list(value)
            for child in range(len(children)):
                for i in range(len(clusters_list)):
                    if (clusters_list[i][0][1] == "INDI" and clusters_list[i][0][2] == children[child]):
                        for j in range(len(clusters_list[i])):
                            if(clusters_list[i][j][1]) == "BIRT":
                                birthdays.append(datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date())
    if(len(birthdays) > 0):
        if len(set(birthdays)) == len(birthdays) - 4:
            return "Error US14: Family " + famID + " has five siblings born at the same time."       
        else:
            return "US14: There are the correct number of siblings in Family " + famID + "."       
    else:
        return "US14: Family " + famID + " does not contain a family with siblings."   
'''
US15 - Sprint 2
Story Name: Fewer than 15 siblings
Description: There should be fewer than 15 siblings in a family
'''
def fewer15Sibs(famID):
    for key, value in siblings.items():
        if (key == famID and len(value) > 1):
            children = list(value)
            if len(children)>=15:
                return("US15: Error, this family has too many sibblings. This family has "+str(len(children))+" sibblings and the max is 15")
    return('No Errors in US15')

'''
US16 - Sprint 2
Story Name: Male last names
Description: All male members of a family should have the same last name
'''

def matchingMaleLastNames(indi_id,fam_id):
    # Check each individual, Append their last name (if its not already there) to the list of families with their family ID in it 
    listOfFamilies=[]
    listOfErrors=[]
    for y in fam_id:
        listOfFamilies.append([y])

    for i in range(len(final_indi)):
        # if(indi_id == final_indi[i][0]):
        if(final_indi[i][2]=='M'):
                temp = final_indi[i][1]
                temp = temp.split("/")
                lastName = temp[1]
                for j in range(len( listOfFamilies)):
                    if (listOfFamilies[j][0] == final_indi[i][7][0]) : 
                        listOfFamilies[j].append(lastName)
    for x in range(len(listOfFamilies)):
        if len(listOfFamilies[x])>2:
            for y in range(1,len(listOfFamilies[x])):
                if listOfFamilies[x][y]!= listOfFamilies[x][y-1]: 
                    listOfErrors.append ("US16: Error, All of the men in this family "+str(listOfFamilies[x][0])+" do not have the same last name")
    return listOfErrors

'''
US17 - Sprint 3
Story Name: No marriages to descendants
Description: Parents should not marry any of their descendants
'''
def noMarriageDescendant(indID):
    tempSpouse = ''
    children = {}
    for i in range(len(final_indi)):
        if (final_indi[i][0] == indID):
            spouses = final_indi[i][8]
            if (spouses != 'N/A'):
                for j in range(len(spouses)):
                    for k in range(len(familyList)):
                        if (familyList[k][0] == spouses[j]):
                            if (indID == familyList[k][3]):
                                tempSpouse = familyList[k][5]
                            if (indID == familyList[k][5]):
                                tempSpouse = familyList[k][3]
                            if (len(familyList[k][7]) == 0):
                                return 'US17: Individual ' + indID + ' has no descendants. No errors in US17.'
                            else:
                                children = familyList[k][7]
                    if (tempSpouse in children):
                        return ('Error US17: Individual ' + indID + 's spouse is also their descendent')
    return 'No errors in US17'

'''
US18 - Sprint 3
Story Name: Siblings should not marry
Description: Siblings should not marry one another
'''
def siblingsNotMarried(indID):
    children = {}
    tempSpouse = ''
    for i in range(len(final_indi)):
        if (final_indi[i][0] == indID):
            spouses = final_indi[i][8]
            if (final_indi[i][7] == 'N/A'):
                return 'No information given about ' + indID + 's siblings.'
            else:
                child_fam = final_indi[i][7][0]
            if (spouses != 'N/A'):
                for j in range(len(spouses)):
                    for k in range(len(familyList)):
                        if (familyList[k][0] == spouses[j]):
                            if (indID == familyList[k][3]):
                                tempSpouse = familyList[k][5]
                            if (indID == familyList[k][5]):
                                tempSpouse = familyList[k][3]
                        if (familyList[k][0] == child_fam):
                            if (len(familyList[k][7]) == 1):
                                return 'US17: Individual ' + indID + ' has no siblings. No errors in US18.'
                            else:
                                children = familyList[k][7]
                        if (indID in children and tempSpouse in children):
                            return ('Error US18: Individual ' + indID + ' and spouse ' + tempSpouse + ' are siblings.')
    return 'No errors in US18'

'''
US19 - Sprint 3
Story Name: First cousins should not marry
Description: First cousins should not marry one another
'''
# this function will help with US19 and US20
def getCloseFamily(indv_id):
    birthFam = ''
    # finding the birth family id
    for i in range(len(final_indi)):
        if (indv_id  == final_indi[i][0]):
            print("indv is in the final_indv")
            birthFam = final_indi[i][7]     #this has the value of the family now need to get siblings kids
            print("birthfam is "+str(birthFam))
            if(birthFam == "N/A"):
                return "NO BIRTH FAM"
    # finding the siblings of the individual provied 
    listSiblings = []
    for i in range(len(familyList)):
        if (len(birthFam)>0 and birthFam[0]  == familyList[i][0]):
            listSiblings = familyList[i][7]
    listSiblings = list(listSiblings)
    print("list of siblings is "+str(listSiblings))
    # for each sibling in the list that is not the inital indv_id add childern to the list of close family 
    closeFamily = []
    for i in range(len(final_indi)):
        if ((final_indi[i][0] in listSiblings) and (final_indi[i][0]!=indv_id )):
            for j in range(len(familyList)):
                if ((familyList[j][3] == final_indi[i][0]) or (familyList[j][5] == final_indi[i][0])):
                    for k in range(len(familyList[j][7])):
                        closeFamily.append((list(familyList[j][7]))[k])
    return closeFamily

def FirstCousinsChouldNotMarry(indv_id):
    mother_id = ''
    father_id = ''
    birthFamId = ''
    marriedFamId = ''
    spouseId= ''
    for i in range(len(final_indi)):
        if (indv_id  == final_indi[i][0]):
            birthFamId = final_indi[i][7]
            marriedFamId = final_indi[i][8]
    for i in range(len(familyList)):
        if (len(birthFamId)>0 and birthFamId[0]  == familyList[i][0]):
            father_id = familyList[i][3]
            mother_id = familyList[i][5]
        elif (len(marriedFamId)>0 and marriedFamId[0]  == familyList[i][0]):
            if(familyList[i][3]!=indv_id):
                spouseId = familyList[i][3]
            else:
                spouseId = familyList[i][5]
    momSide = getCloseFamily(mother_id)
    dadSide = getCloseFamily(father_id)
    if (marriedFamId == [] or (momSide == "NO BIRTH FAM" and dadSide== "NO BIRTH FAM") or (momSide == [] and dadSide== [])):
        return (str(indv_id) + " is not married to a cousin.")
    elif((spouseId in momSide) or (spouseId in dadSide)):
        return ("Error US19: individual " + str(indv_id) + " is married to a cousin.")
    else:
        return (str(indv_id) + " is not married to a cousin.")
    
'''
US20 - Sprint 3
Story Name: Aunts and uncles
Description: Aunts and uncles should not marry their nieces or nephews
'''
def AuntsAndUncles(indv_id):
    niecesAndNephews = getCloseFamily(indv_id)
    marriedFamId = ''
    spouseId = ''
    for i in range(len(final_indi)):
        if (indv_id  == final_indi[i][0]):
            marriedFamId = final_indi[i][8]
    for i in range(len(familyList)):
        if (marriedFamId[0]  == familyList[i][0]):
            if(familyList[i][3]!=indv_id):
                spouseId = familyList[i][3]
            else:
                spouseId = familyList[i][5]
    if (niecesAndNephews == "NO BIRTH FAM" or niecesAndNephews==[] or spouseId == ''):
        return (str(indv_id) + " is not married to a niece or nephew.")
    elif (spouseId in niecesAndNephews):
        return ("Error US20: individual " + str(indv_id) + " is married to a niece or nephew.")
'''
US21 - Sprint 3
Story Name: Correct gender for role
Description: Husband in family should be male and wife in family should be female
'''

def correctGenderRole(FAM_ID):
    husb_id = ""
    wife_id = ""
    for i in range(len(familyList)):
        if (FAM_ID == familyList[i][0]):
            husb_id = familyList[i][3]
            wife_id = familyList[i][5]
    for i in range(len(indi_list)):
        if (husb_id != "" and husb_id != "N/A" and indi_list[i][0] == husb_id):
            if (indi_list[i][2] == "N/A"):
                return "US21: Sex for husband " + husb_id + " in family " + FAM_ID + " is unknown."
            if (indi_list[i][2] != "M"):
                return "Error US21: Husband " + husb_id + " in family " + FAM_ID + " is not male."
        if (husb_id != "" and husb_id != "N/A" and indi_list[i][0] == wife_id):
            if (indi_list[i][2] == "N/A"):
                return "US21: Sex for wife " + wife_id + " in family " + FAM_ID + " is unknown."
            if (indi_list[i][2] != "F"):
                return "Error US21: Wife " + wife_id + " in family " + FAM_ID + " is not female."
    return "US21: Husband and wife for family " + FAM_ID + " have correct gender roles."

'''
US22 - Sprint 3
Story Name: Unique IDs
Description: All individual IDs should be unique and all family IDs should be unique
'''

def uniqueIDsFams(FAM_ID):
    family_ids = {}
    for i in range(len(familyList)):
        if familyList[i][0] in family_ids:
            family_ids[familyList[i][0]] = family_ids[familyList[i][0]] + 1
        else:
            family_ids[familyList[i][0]] = 1
    if (FAM_ID in family_ids):
        if (family_ids[FAM_ID] == 1):
            return "US22: Family ID " + FAM_ID + " is unqiue."
        elif (family_ids[FAM_ID] > 1):
            return "Error US22: Family ID " + FAM_ID + " is not unqiue."
    else:
        return "US22: Family ID " + FAM_ID + " does not exist."

def uniqueIDsIndis(INDI_ID):
    indi_ids = {}
    for i in range(len(indi_list)):
        if indi_list[i][0] in indi_ids:
            indi_ids[indi_list[i][0]] = indi_ids[indi_list[i][0]] + 1
        else:
            indi_ids[indi_list[i][0]] = 1
    if (indi_ids[INDI_ID]):
        if (indi_ids[INDI_ID] == 1):
            return "US22: Individual ID " + INDI_ID + " is unqiue."
        elif (indi_ids[INDI_ID] > 1):
            return "Error US22: Individual ID " + INDI_ID + " is not unqiue."
    else:
        return "US22: Individual ID " + INDI_ID + " does not exist."
'''
US23 - Sprint 3
Story Name: Unique name and birth date
Description: No more than one individual with the same name and birth date should appear in a GEDCOM file
'''

#name and birthday can't be the same for more than one person 
def uniqueIndiv(INDI_ID):
    for i in range(len(indi_list)):
        if indi_list[i][0] == INDI_ID:
            currInd = []
            currInd.append(indi_list[i][1])
            currInd.append(indi_list[i][3])
    for i in range(len(indi_list)):
        tempInd = []
        tempInd.append(indi_list[i][1])
        tempInd.append(indi_list[i][3])
        if currInd == tempInd and INDI_ID != indi_list[i][0]:
            return "ERROR US23: Individual:  " + str(currInd[0]) + " exists multiple times within the file ."
    return "US23: no error found"    

'''
US24 - Sprint 3
Story Name: Unique families by spouses
Description: No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
'''
def uniqueFamily(FAM_ID):
    currFam =[]
    for i in range(len(familyList)):
        if familyList[i][0] == FAM_ID:
            currFam = []
            currFam.append(familyList[i][1])
            currFam.append(familyList[i][4])
            currFam.append(familyList[i][6])
    if currFam == []:
        return "Error US24 Fam ID not in file"    
            
    for i in range(len(familyList)):
        tempFam = []
        tempFam.append(familyList[i][1])
        tempFam.append(familyList[i][4])
        tempFam.append(familyList[i][6])
        if currFam == tempFam and FAM_ID != familyList[i][0]:
            return "ERROR US24: Family:  " + str(FAM_ID) + " exists as more than one family with the same spouses by name and the same marriage date."
    return "US24: no error found"  

'''
US27 - Sprint 4
Story Name: Include individual ages
Description: Include person's current age when listing individuals
'''
def individualAges(Indv_ID):
    for i in range(len(final_indi)):
        if final_indi[i][0] == Indv_ID:
            return "US27: Individul " + str(final_indi[i][1]) + " ("+str(final_indi[i][0])+ ") has the age of "+ str(final_indi[i][4])+"."
    return "US27: "+str(Indv_ID)+" not found."

'''
US28 - Sprint 4
Story Name: Order siblings by age
Description: List siblings in families by decreasing age, i.e. oldest siblings first
'''
def orderSiblingsByAge(Fam_ID):
    siblings = True
    for i in range(len(familyList)):
        if familyList[i][0] == Fam_ID:
            siblings=familyList[i][7]
    if siblings==True:
        return "US28: Family "+str(Fam_ID)+ " not found."
    if siblings == {}:
        return "US28: Family "+str(Fam_ID)+ " has not children."
    Age = []
    for i in range(len(final_indi)):
        if final_indi[i][0] in siblings:
            if final_indi[i][3] == 'N/A':
                return "US28: Family "+str(Fam_ID)+ " missing children birthdays."
            else:
                Age.append((final_indi[i][0],final_indi[i][3]))
    # Sorting the array
    n = len(Age)
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if Age[j][1] > Age[j + 1][1]:
                Age[j], Age[j + 1] = Age[j + 1], Age[j]
    Age.reverse()
    result = [tup[0] for tup in Age]
    return "US28: Family "+str(Fam_ID)+ " has children " + str(result) +" listed oldest to youngest."



if __name__ == '__main__':
    for i in range(len(familyList)):
        print(uniqueFamily(familyList[i][0]))
        print(childDuringMarriage(familyList[i][0]))
        print(divorceBeforeDeath(familyList[i][0]))
        print(marrigeBeforeDivorce(familyList[i][0]))
        print(siblingSpacing(familyList[i][0]))
        print(multipleBirths(familyList[i][0]))
        print(uniqueIDsFams(familyList[i][0]))
        print(correctGenderRole(familyList[i][0]))
        print(orderSiblingsByAge(familyList[i][0]))

    for i in range(len(final_indi)):
        print(uniqueIndiv(final_indi[i][0]))
        print(deathLessThan150(final_indi[i][0]))
        print(birthBeforeDeath(final_indi[i][0]))
        print(birthBeforeMarr(final_indi[i][0]))
        print(marriageAfter14(final_indi[i][0]))
        print(birthBeforeParentsDeath(final_indi[i][0]))
        print(uniqueIDsIndis(final_indi[i][0]))
        print(FirstCousinsChouldNotMarry(final_indi[i][0]))
        print(AuntsAndUncles(final_indi[i][0]))
        print(noMarriageDescendant(final_indi[i][0]))
        print(individualAges(final_indi[i][0]))

    
