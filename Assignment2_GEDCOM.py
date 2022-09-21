from prettytable import PrettyTable

file = open('test.ged', 'r')

individuals = PrettyTable()
individuals.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

families = PrettyTable()
families.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

acceptable_tags_0 = ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE']
acceptable_tags_1 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
acceptable_tags_2 = ['DATE']

for line in file:

    words = line.split()

    if(len(words) == 0):
        continue

    if (words[0] == '0'):

        if (words[2] == "FAM"):    
            print("do something")
        elif (words[2] == "INDI"):
            print("do something")

 

            