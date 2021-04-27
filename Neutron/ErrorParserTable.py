import sys
import pandas as pd
import numpy as np
from IPython.display import display

first = [[";","void","char","short","int","long","float","double","string"],
["void","char","short","int","long","float","double","string"],
["Name"],
["void","char","short","int","long","float","double","string"],
["void","char","short","int","long","float","double","string"],
["''",";","void","char","short","int","long","float","double","string"],
[",","''"],
["void","char","short","int","long","float","double","string"],
["void","char","short","int","long","float","double","string"],
["''","if","void","char","short","int","long","float","double","string","while","Name","return"],
["return"],
["Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
["Name"],
["(","="],
["if"],
["else","''"],
["Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
["Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
["==","<=",">=","!=",">","<"],
["void","char","short","int","long","float","double","string"],
["=","''"],
["CharacterValue","StringValue","FloatValue","IntegerValue"],
["("],
[",","''","Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
[",","''","Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
["Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
["''","+","-","/","*","&","|","^","%"],
["while"],
["+","-","/","*","&","|","^","%"],
["="],
["+","-","/","*","&","|","^","%"]
]

follows = [[],
[";","void","char","short","int","long","float","double","string"],
["("],
["Name"],
["Name"],
[")"],
[")"],
[")",","],
["Name"],
["}"],
[";"],
[";"],
[";"],
[";"],
["}","if","void","char","short","int","long","float","double","string","while","Name","return"],
["}","if","void","char","short","int","long","float","double","string","while","Name","return"],
[")"],
["==","<=",">=","!=",">","<",")","",",","Name","CharacterValue","StringValue","FloatValue","IntegerValue","+","-","/","*","&","|","^","%",";"],
["Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
[";"],
[";"],
["==","<=",">=","!=",">","<",")",",","Name","CharacterValue","StringValue","FloatValue","IntegerValue","+","-","/","*","&","|","^","%",";"],
[";"],
[")"],
[")"],
[",",")","Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
[",",")","Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
["}","if","void","char","short","int","long","float","double","string","while","Name","return"],
[",",")","Name","CharacterValue","StringValue","FloatValue","IntegerValue"],
[";"],
["Name","CharacterValue","StringValue","FloatValue","IntegerValue"]
]

nonTerminals= ["Functions","Function","FunctionName",
"FunctionType","type-specifier","parameters","D","parameter",
"dataType","content","returnStatement","temp","Akshat",
"Aryan","conditionalStatement","Extra","condition",
"NameOrValue","doubleOperator","variableInitialization",
"moreVariable","valueVariable","functionCall",
"arguments","names","NameOrValueOrOperations","Decide",
"loop","operationRHS","operation","operators"
]

terminals = [";","(",")","{","}","Name","void","char",
"short","int","long","float","double","string",",",
"return","if","else","==","<=",">=","!=",">","<",
"=","CharacterValue","StringValue","FloatValue",
"IntegerValue","","while","+","-","/","*","&",
"|","^","%","end"]

print(len(nonTerminals),len(follows),len(first))
#row1 =[[;,void,char,short,int,long,float,double,string}	{end}	Functions	Functions -> ;						Functions -> Function Functions	Functions -> Function Functions	Functions -> Function Functions	Functions -> Function Functions	Functions -> Function Functions	Functions -> Function Functions	Functions -> Function Functions	Functions -> Function Functions

col1 = ["Functions -> ;","","","","","","","","","","","","","","",
"","","","","","moreVariable -> ''","","","","","","","","","",""]

col2 = ["","","","","","","","","","","","","","Aryan -> functionCall","",
"","","","","","","","functionCall -> ( arguments )","","","","",
"","","",""]

col3 = ["","","","","","parameters -> ''","D -> ''","","","","","","","","","","","","","",
"","","","arguments -> names","names -> ''","","Decide -> ''",
"","","",""]

df = pd.DataFrame()
df["First"] = first
df["Follows"] = follows
df["NonTerminals"]=nonTerminals
df[";"]=col1
df["("] = col2
df[")"] = col3
col4 = ["","","","","","","","","","","","","","","","","","","","",
"","","","","","","","","","",""]
df["{"] = col4

col5 = ["","","","","","","","","","content -> ''","","","","","",
"Extra -> ''","","","","","","","","","","","","","","",""]
df["}"] = col5

col6 = ["","","FunctionName -> Name","","","","","","","content -> Akshat ; content",
"","temp -> Name functionCall","Akshat -> Name Aryan","","","Extra -> ''",
"condition -> NameOrValue doubleOperator NameOrValue","NameOrValue -> Name",
"","","","","","arguments -> names","	names -> NameOrValueOrOperations names",
"NameOrValueOrOperations -> NameOrValue Decide","Decide -> ''","","","",""]
df["Name"] = col6

col7 = ["Functions -> Function Functions","Function -> FunctionType FunctionName ( parameter ) { content }",
"","FunctionType -> type-specifier","type-specifier -> void","parameters -> parameter D",
"","parameter -> dataType Name","dataType -> type-specifier","content -> variableInitialization ; content",
"","","","","","Extra -> ''","","","","variableInitialization -> type-specifier Name moreVariable",
"","","","","","","","","","",""]
df["void"]=col7

col8 = col7
df["char"] = col8

col9 = col7
df["short"] = col9

col10 = col7
df["int"] = col10

col11 = col7
df["long"] = col11

col12 = col7
df["float"] = col12

col13 = col7
df["double"] = col13

col14 = col7
df["string"] = col14

col15 = ["","","","","","","D -> , parameters","","","","","","","",
"","","","","","","","","","arguments -> names","names -> , NameOrValueOrOperations",
"","Decide -> ''","","","",""]
df[","] = col15

col16 = ["","","","","","","","","","content -> returnStatement ; content",
"returnStatement -> return temp","","","","","Extra -> ''","","","","",
"","","","","","",'','',"","",""]
df["return"]=col16

col17 = ["","","","","","","","","","content -> conditionalStatement content",
"","","","","conditionalStatement -> if ( condition ) { content } Extra","Extra -> ''","","","","",
"","","","","","",'','',"","",""]
df["if"] = col17

col18 = ["","","","","","","","","","",
"","","","","","Extra -> else { content }","","","","",
"","","","","","",'','',"","",""]
df["else"] = col18

col19 = ["","","","","","","","","","",
"","","","","","","","","doubleOperator -> ==","",
"","","","","","",'','',"","",""]
df["=="] = col19

col20 = col19
df["<="] = col20

col21 = col19
df[">="] = col21

col22 = col19
df["!="] = col22

col23 = col19
df[">"] = col23

col24 = col19
df["<"] = col24

col25 = ["","","","","","","","","","","","","","Aryan -> operation",
"","","","","","","moreVariable -> = valueVariable","","","","",
"","","","","operation -> = NameOrValue operationRHS",""]
df["="] = col25

col26 = ["","","","","","","","","","","","temp -> valueVariable",
"","","","","condition -> NameOrValue doubleOperator NameOrValue",
"NameOrValue -> valueVariable","","","","valueVariable -> CharacterValue",
"","arguments -> names","names -> NameOrValueOrOperations names",
"NameOrValueOrOperations -> NameOrValue Decide","Decide -> ''",
"","","",""]
df["CharacterValue"] = col26

col27 = col26
df["StringValue"] = col27

col28 = col26
df["FloatValue"] = col28

col29 = col26
df["IntegerValue"] = col29

col30 = ["","","","","","","","","","content -> loop content",
"","","","","","Extra -> ''","","","","","","","","","","","",
"loop -> while ( condition ) { content }","","",""]
df["while"]=col30

col31 = ["","","","","","","","","","","","","","","","","","","","",
"","","","","","","Decide -> operationRHS","",
"operationRHS -> operators NameOrValue","","operators -> +"]
df["+"]=col31

col32 = col31
df["-"] =  col32

col33 = col31
df["/"] =  col33

col34 = col31
df["*"] =  col34

col35 = col31
df["&"] =  col35

col36 = col31
df["|"] =  col36

col37 = col31
df["^"] =  col37

col38 = col31
df["%"] =  col38

col32 = col4
df["end"] =  col32

l1=len(df)

for i in range(0,l1):
    tempFollows = df.loc[i,'Follows']
    tempFollows.append("end")
    df.at[i,'Follows']=tempFollows

df = df.replace(r'^\s*$', np.NaN, regex=True)

print(df[";"])

columns = df.columns.values.tolist()
print(columns)

l2=len(df.columns)
print(l1,l2)

s1,s2 = "scan","pop"
s3 = str(s1)
s4 = str(s2)

df = df.astype(str)


for i in range(0,l1):
    tempFollows = []
    tempFollows = df.loc[i,'Follows']
    for j in range(3,l2):
        lo = columns[j]
    #    a = df.loc[i,j]
    #    print(a)
        if df.iloc[i][lo] == "nan":
            if columns[j] not in tempFollows:
                df.iloc[i][df.columns.get_loc(lo)]=s3
                df.at[i, lo]=s1
                yoyo = 4
            if columns[j] in tempFollows:
            #    df.iloc[i][lo]=s2
                df.at[i, lo]=s4

print("done")
print(df["if"])

input_lines = []
with open('input.txt', 'r') as file:
     input_lines = [line.strip() for line in file]
print(input_lines)

#manguage=input("Enter your language ")

language = input_lines
initially = len(language)
language.append("end")
print("length of language is",len(language))
pond1 = []
temp = []
stack = []
stack.append("end")
stack.append("Functions")
mento = []
#mento.append(stack)
temp.append(stack[1:])
temp.append(language)
temp.append("")
pond1.append(temp)
#print(mento)
start=0
while 1 == 1:
    pond2 = []
#    print(start)
    if start > initially:
        break
    token = language[start]
    a = stack[len(stack)-1]
    print(token,a)
    if a == "end":
        break
    if a in terminals:
        stack.pop()
        start=start+1
        pond2.append(stack[1:])
        pond2.append(language[start:])
        pond2.append("")
        mento.append(stack[1:])
        pond1.append(pond2)
        continue

    ro,co=0,0
    for i in range(0,l1):
        if df.iloc[i][2] == a:
            ro=i
            break

    for j in range(0,l2):
        if columns[j] == token:
            co=j
            break


    rule = df.iloc[ro][co]
    if rule == "scan":
        start = start + 1
        error = "Error, parsing " + token
        pond2.append(stack[1:])
        pond2.append(language[start:])
        pond2.append(error)
        pond1.append(pond2)
        print(start,"scan")
        continue
    if rule == "pop":
        stack.pop()
        error = "Error, popping " + a
        pond2.append(stack[1:])
        pond2.append(language[start:])
        pond2.append(error)
        pond1.append(pond2)
        print(start,"pop")
        continue
    t = rule.split()
    stack.pop()

    for j in range(len(t)-1,1,-1):
        if t[j] != "''":
            stack.append(t[j])

    #print(stack,"stack ",rule,"rule")
    pond2.append(stack[1:])
    mento.append(stack[1:])
    pond2.append(language[start:])
    pond2.append(rule)
#    print(pond2)
    pond1.append(pond2)
    #print(pond1)

print(pond1[0])
colums = ["Stack","Input","Rule"]
#print(pond1)

df2 = pd.DataFrame(pond1,columns=colums)
#df2.insert(0,"stack2",mento)

print(df2)

display(df2)
#df.to_csv('file1.csv')
df2.to_csv('file3.csv')

#np_array=df2.to_numpy()
#np.savetxt('Yes.txt', np_array, fmt='%s')

#np.savetxt(r'abcd.txt', df2.values, fmt='%d')
