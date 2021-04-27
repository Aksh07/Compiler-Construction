#Aryan Sharma 						2018A7PS0245H
#Akshat Bajpai 						2018A7PS0498H
#Sai Chaitanya Nallamala 			2018A7PS0503H
#Sruthi Reddy Ailuri				2018A7PS0160H

import sys

TokenDict = {'char' : 1, 'int' : 2 , 'float': 3 , 'string': 4 , 'boolean': 5, 'if': 6 , 'else': 7 , 'while': 8 , 'true':9 , 'false': 10,
                '+' : 11 , '-' : 12 , '*' : 13 , '/' : 14 , '%' : 15 , '=' : 16 , '==' : 17 , '>' : 18 , '<' : 19 , '>=' : 20 , '<=' : 21 ,
                 '!=' : 22 , '&&' : 23 , '||' : 24 , '!' : 25 , '?' : 26 , ':' : 27 , '{' : 28 , '}' : 29 , '(' : 30 , ')' : 31 , '[' : 32 , ']' : 33 ,
                  ';' : 34 , ',' : 35 , 'return' : 37, 'void' : 38, '^' : 42, 'for':43}

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

finalList = []
variables = []          #Stores all variables declared
intVariables = []       #Stores the integer variables declared
noOfLines = 0           #Store the Line Number
count = 0               #Stores the index of the token in the words list, i.e., in each line
comment = 0             #flag for checking multiline comment
for line in fhand :
    noOfLines += 1
    words = line.split()            # List storing tokens in each line
    count = 0

    if line.startswith("//") :      #Skipping the line if it starts with double slashes
        continue

    for word in words :
        count += 1
        if word.startswith("/*") :  # Skipping until we encounter */
            comment = 1

        if word == "*/" :
            comment = 0
            continue

        if comment  == 1 :
            continue

        if word == 'write':
            finalList.append('Name')
            print("Token 44, string write, line number " + str(noOfLines))
            continue

        if word in TokenDict.keys() :       #Checking if the keyword belongs to the Token Dictionary
            keyValue = TokenDict[word]
            print("Token " + str(keyValue) + ", string " + word + ", line number " + str(noOfLines))
            if keyValue == 39 or keyValue == 37:
                finalList.append('Name')
            else:
                finalList.append(str(word))
            #flag =1
        else :          # for checking if it's a variable or not
            if count > 1: # for checking if it has a data type
                if word not in variables:  # till now the word is not in the list of variables
                    variables.append(word)
                    try: #check the variable if it is a number print it but not store it
                        num = float(word)
                        try :           #checking if the float we got is integer or not
                            num = int(word)
                            print("Token 36, string " + str(num) + ", line number " + str(noOfLines))
                            finalList.append('IntegerValue')
                            variables.pop()     #Since it's a number we a poping it from the variables list
                        except:         # if the number is not an integer checking the variable data type declaration
                            if words[count - 3] in intVariables :
                                print("WRONG ASSIGNMENT TO DATA TYPE:\n    Float value cannot be assigned to Int variable " +words[count-3]+"... in line number " + str(noOfLines))
                                continue
                            print("Token 36, string " + str(num) + ", in line number " + str(noOfLines))
                            finalList.append('FloatValue')
                            variables.pop()
                    except:             #checking for tokens other than the numbers
                            try:
                                keyValue = int(TokenDict.get(words[count - 2]))         #Storing the value for the key word if it exist
                                if keyValue < 6:   # checking if the word is a dataype which are stored in values lesser than 6
                                    print("Token 36, string " + word + ", line number " + str(noOfLines))
                                    #finalList.append(str(word))
                                    if keyValue == 2 :
                                        intVariables.append(word)
                                        finalList.append('Name')
                                    elif keyValue == 1:
                                        finalList.append('Name')
                                    elif keyValue == 3:
                                        finalList.append('Name')
                                    elif keyValue == 4:
                                        finalList.append('Name')
                                    else:
                                        finalList.append('IntegerValue')
                                else:
                                    variables.pop()
                                    print('ERROR ' + words[count-2] + " NOT A DATATYPE, in line number " + str(noOfLines))
                                    finalList.append('Name')
                            except:
                                print('ERROR NO DATATYPE DEFINED FOR '+ word +", in line number " + str(noOfLines))
                else:
                    if int(TokenDict.get(words[count - 2])) < 6:        #checking if that variable is already defined previously
                        print('ERROR VARIABLE '+ word + " ALREADY IN USE, in line number " + str(noOfLines))
                    else :
                        print("Token 36, string " + word + ", line number " + str(noOfLines))
                        finalList.append("Name")
            else:
                if word not in variables:
                    print('ERROR VARIABLE '+ word +" NOT DEFINED, in line number " + str(noOfLines))
                    finalList.append('Name')
                else:
                    print("Token 36, string " + word + ", line number " + str(noOfLines))
                    finalList.append('Name')
        #print(str(noOfLines)+ ' ' + str(count) )
print(finalList)

with open('input.txt', 'w') as f:
    for item in finalList:
        f.write("%s\n" % item)
