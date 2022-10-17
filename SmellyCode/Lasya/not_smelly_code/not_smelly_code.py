from typing import final
from unittest.result import failfast
from prettytable import PrettyTable
from datetime import datetime, date, timedelta

file = open('SmellyCode/Lasya/not_smelly_code/smelly_test.ged', 'r')
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
                else:
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
                MARR = 0
                DIV = 0
                for j in range(len(clusters_list[i])):
                    if (clusters_list[i][j][1] == "MARR"):
                        MARR = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()
                    if (clusters_list[i][j][1] == "DIV"):
                        DIV = datetime.strptime(clusters_list[i][j+1][2], '%d %b %Y').date()
                    if (DIV != 'N/A' and DIV != 0):
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
                else:
                    return "No errors in " + user_story_num + " for family " + id



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
                    # print(id)
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
            print(issues)
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

def last30(date):
    last30 = []

    today = datetime.strptime(date, '%d %b %Y').date()
    start = datetime(today.year, today.month, today.day)                                                                                                                                                                    
    for day in range(1, 31): 
        last30.append(start-timedelta(days=day))
    
    return last30

def dates_in_last30_days(last_30_days, birth = False, death = False):
    dates_list = []

    for i in range(len(final_indi)):
        if (birth == True):
            if (final_indi[i][3]!='N/A'):
                birthday_date = datetime.strptime(final_indi[i][3], '%d %b %Y').date()
                birthday_datetime = datetime(birthday_date.year, birthday_date.month, birthday_date.day)
                if (birthday_datetime in last_30_days):
                    dates_list.append(final_indi[i][0])
        if (death == True):
            if (final_indi[i][6]!='N/A'):
                death_date = datetime.strptime(final_indi[i][6], '%d %b %Y').date()
                death_datetime = datetime(death_date.year, death_date.month, death_date.day)
                if (death_datetime in last_30_days):
                    dates_list.append(final_indi[i][0])
    return dates_list

def recentBirths(date_str):
    days = last30(date_str)
    recentBirth = dates_in_last30_days(days, birth = True)

    if (len(recentBirth) > 0):
        return "US15: Recent Births from " + date_str + " include " + str(recentBirth) + "."
    else: 
        return "No recent births."

def recentDeaths(date_str):
    days = last30(date_str)
    recentDeath = dates_in_last30_days(days, death = True)
            
    if (len(recentDeath) > 0):
        return "US15: Recent Deaths from " + date_str + " include " + str(recentDeath) + "."
    else: 
        return "No recent deaths." 

if __name__ == '__main__':

    fam_ids = ["F03", "F08", "F05", "F06"]
    indi_ids = ["I01", "I02", "I03", "I04", "I05", "I06", "I07", "I08", "bi00"]
    
    #print(parentsNotTooOld('F05'))
    # print(datesBeforeCurrent("I01"))
    #print(recentBirths("17 OCT 2022"))
    #print(recentDeaths("17 OCT 2022"))
    
    print(recentBirths("17 OCT 2022"))
    print(recentBirths("1 NOV 2002"))
    print(recentBirths("24 FEB 1935"))
    print(recentBirths("10 JAN 2022"))

    print(recentDeaths("17 OCT 2022"))
    print(recentDeaths("26 JAN 1935"))
    print(recentDeaths("12 OCT 2002"))
    print(recentDeaths("1 JAN 2010"))


    #for i in range(len(fam_ids)):
    #     print(childDuringMarriage(fam_ids[i]))
    #     print(divorceBeforeDeath(fam_ids[i]))
    #     print(marrigeBeforeDeath(fam_ids[i]))
    #     marrigeBeforeDivorce(fam_ids[i])
    #    print(siblingSpacing(fam_ids[i]))
    #    print(multipleBirths(fam_ids[i]))
        
    # for i in range(len(indi_ids)):
    #     deathLessThan150(indi_ids[i])
    #     birthBeforeDeath(indi_ids[i])
    #     birthBeforeMarr(indi_ids[i])

