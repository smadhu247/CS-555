file = open('test.txt', 'r')

acceptable_tags_0 = ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE']
acceptable_tags_1 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
acceptable_tags_2 = ['DATE']

for line in file:
    print("--> ", line.rstrip("\n"))
  
    words = line.split()

    if (words[0] == '0'):
        if (words[1] in acceptable_tags_0):
            if (words[1] == 'HEAD' or words[1] == 'TRLR' or words[1] == 'NOTE'):
                level = words[0]
                tag = words[1]
                words.pop(0)
                words.pop(0)
                if (len(words) == 0):
                    print("<-- "+level+"|"+tag+"|Y")
                else:
                    sent = " ".join(words)
                    print("<-- "+level+"|"+tag+"|Y|"+sent)
            else:
                level = words[0]
                tag = words[1]
                words.pop(0)
                words.pop(0)
                if (len(words) == 0):
                    print("<-- "+level+"|"+tag+"|N")
                else:
                    sent = " ".join(words)
                    print("<-- "+level, "|"+tag+"|N|"+sent)
        elif (words[2] in acceptable_tags_0):
            if (words[2] == 'INDI' or words[2] == 'FAM'):
                print("<-- "+words[0].strip()+"|"+words[2].strip()+"|Y|"+words[1].strip())
            else:
                level = words[0]
                tag = words[2]
                words.pop(0)
                words.pop(1)
                if (len(words) == 0):
                    print("<-- "+level+"|"+tag+"|N")
                else:
                    sent = " ".join(words)
                    print("<-- "+level, "|"+tag+"|N|"+sent)
        else:
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if (len(words) == 0):
                    print("<-- "+level+"|"+tag+"|N")
            else:
                sent = " ".join(words)
                print("<-- "+level+"|"+tag+"|N|"+sent)

    elif (words[0] == '1'):
        if (words[1] in acceptable_tags_1):
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if(len(words) == 0):
                print("<-- "+level+"|"+tag+"|Y")
            else:
                sent = " ".join(words)
                print("<-- "+level+"|"+tag+"|Y|"+sent)
        else:
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if(len(words) == 0):
                print("<-- "+level+"|"+tag+"|N")
            else:
                sent = " ".join(words)
                print("<-- "+level+"|"+tag+"|N|"+sent)

    elif (words[0] == '2'):
        if (words[1] in acceptable_tags_2):
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if(len(words) == 0):
                print("<-- "+level+"|"+tag+"|Y")
            else:
                sent = " ".join(words)
                print("<-- "+level+"|"+tag+"|Y|"+sent)
        else:
            level = words[0]
            tag = words[1]
            words.pop(0)
            words.pop(0)
            if(len(words) == 0):
                print("<-- "+level+"|"+tag+"|N")
            else:
                sent = " ".join(words)
                print("<-- "+level+"|"+tag+"|N|"+sent)
    else:
        print("<-- INVALID LEVEL")