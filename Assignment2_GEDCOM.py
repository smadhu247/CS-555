from prettytable import PrettyTable

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
#notes/extra information. Third index is a boolean indicating if this line was level 0.

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
                    modified_file.append(temp)
                else:
                    sent = " ".join(words)
                    temp.append(level)
                    temp.append(tag)
                    temp.append(sent)
                    temp.append(True)
                    #print(temp)
                    modified_file.append(temp)

        elif (words[2] in acceptable_tags_0):
            if (words[2] == 'INDI' or words[2] == 'FAM'):
                temp = []
                temp.append(words[0].strip())
                temp.append(words[2].strip())
                temp.append(words[1].strip())
                temp.append(True)
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
                    modified_file.append(temp)
                else:
                    sent = " ".join(words)
                    temp.append(level)
                    temp.append(tag)
                    temp.append(sent)
                    temp.append(True)
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
                modified_file.append(temp)            
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(True)
                modified_file.append(temp)
    
    elif (words[0] == '1'):
        if (words[1] in acceptable_tags_1):
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
                modified_file.append(temp)
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(False)
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
                modified_file.append(temp)
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(False)
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
                modified_file.append(temp)
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(False)
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
                modified_file.append(temp)
            else:
                sent = " ".join(words)
                temp.append(level)
                temp.append(tag)
                temp.append(sent)
                temp.append(False)
                modified_file.append(temp)

print (modified_file)

'''
for line in file:
=======
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
        

    # if (clusters_list[i][0][1] == "INDI"):
>>>>>>> 16379bb5c40e2100f51e6cad7b2c961289450e1b


print(families)
    
'''
            