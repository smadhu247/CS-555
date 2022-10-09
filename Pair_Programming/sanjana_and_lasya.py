from typing import final
from prettytable import PrettyTable
from datetime import datetime, date, timedelta
import pandas as pd

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
                try:
                    birthday = datetime.strptime(modified_file[i+1][2], '%d %b %Y').date()
                    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
                except ValueError:
                    age = "N/A"
                indi[4] = age

        if (modified_file[i][1] == 'DEAT'):
            indi[5] = False
            if (modified_file[i+1][1] == 'DATE'):
                indi[6] = modified_file[i+1][2]
                try:
                    death = datetime.strptime(modified_file[i+1][2], '%d %b %Y').date()
                    death_age = death.year - birthday.year - ((death.month, death.day) < (birthday.month, birthday.day))
                except ValueError:
                    death_age = "N/A"
                indi[4] = death_age

        if (modified_file[i][1] == 'FAMC'):
            famc_list = []
            famc = i
            
            if (modified_file[i][4] == 'famc'):
                famc_list.append(modified_file[i][2])
                modified_file[i][4] = 'famc seen'
                
                while(modified_file[famc][1] == 'FAMC' and modified_file[famc+1][1] == 'FAMC'):
                    famc_list.append(modified_file[famc+1][2])
                    modified_file[famc+1][4] = 'famc seen'
                    famc = famc+1
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
    indi_list.append(indi)        

final_indi = []
for i in range(len(indi_list)):
    if (indi_list[i] in final_indi):
        continue
    else:
        final_indi.append(indi_list[i])

individuals.add_rows(
    final_indi
)

print(individuals)

j = 1
for i in range(len(modified_file)):  
    if (modified_file[i][0] == '0' and modified_file[i][1] == "FAM"):
        j = j + 1     
    elif (modified_file[i][0] == '0' and modified_file[i][1] == "INDI"):
        j = j + 1 
    modified_file[i].append(j)

# print(modified_file)

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

print(families) 

# Sanjana's User Story: Reject illegitimate dates
def rejectBadDates():
    isInvalid = False
    return_list = ""
    for i in range(len(clusters_list)):
        for j in range(len(clusters_list[i])):
            if clusters_list[i][j][1] == 'DATE':
                try:
                    date = datetime.strptime(clusters_list[i][j][2], '%d %b %Y').date()
                except (ValueError, TypeError):
                    isInvalid = True
                    return_list = return_list + "Error: " + clusters_list[i][j][2] + " is invalid.\n"
    if (isInvalid is True):
        return return_list
    else:
        return "All dates are valid"
                
# Lasya's User Story: List births from last 30 days
def recentBirths():
    last30 = []
    recentBirth = []

    start = datetime(today.year, today.month, today.day)                                                                                                                                                                      
    for day in range(1, 31): 
        last30.append(start-timedelta(days=day))
        
    for i in range(len(final_indi)):
        if (final_indi[i][3]!='N/A'):
            birthday_date = datetime.strptime(final_indi[i][3], '%d %b %Y').date()
            birthday_datetime = datetime(birthday_date.year, birthday_date.month, birthday_date.day)
            if (birthday_datetime in last30):
                recentBirth.append(final_indi[i][0])
            
    return recentBirth

# Pair Programming User Story: List deaths from last 30 days
def recentDeaths():
    last30 = []
    recentDeath = []

    start = datetime(today.year, today.month, today.day)                                                                                                                                                                      
    for day in range(1, 31): 
        last30.append(start-timedelta(days=day))

    for i in range(len(final_indi)):
        if (final_indi[i][6]!='N/A'):
            death_date = datetime.strptime(final_indi[i][6], '%d %b %Y').date()
            death_datetime = datetime(death_date.year, death_date.month, death_date.day)
            if (death_datetime in last30):
                recentDeath.append(final_indi[i][0])
            
    return recentDeath

# Results:
# print(rejectBadDates())
# print(recentBirths())
# print(recentDeaths())