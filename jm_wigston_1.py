#!/usr/local/bin/python
# -*- coding: utf-8 -*-

textfile= "D:/development/wigston/wigston_text2.txt"

fhand1 = open(textfile)
wholefile = ""
startposition = 0

header = "number|text|date|\n"
outputtext = header

t= 0

for line in fhand1:
    t = t +1
    wholefile = wholefile + line

print (t, len(wholefile))

i = 1
finalposition = 1

while i < 1155:
    searchtarget = str(i) + "."
    endposition = wholefile.find(searchtarget, startposition)

    if endposition > startposition:
        section = wholefile[startposition:endposition]
        section = section.replace("\n", " ")

        #date text
        numberlength = len(searchtarget)
        datephrase = section[numberlength:10+numberlength]



        outputtext = outputtext + str(i-1) + "|" + section + "|" + datephrase + "|\n"
        startposition = endposition
        i += 1
        print (i, len(section), datephrase)

    else:
        print ("skipped", i, startposition, wholefile[startposition:100]) 
        i +=1

        with open('wigston.csv', 'w') as f:
            f.write(outputtext)
        
        exit()


print ("complete")

with open('wigston.csv', 'w') as f:
    f.write(outputtext)