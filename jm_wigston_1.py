#!/usr/local/bin/python
# -*- coding: utf-8 -*-

textfile= "D:/development/wigston/wigston_text2.txt"

fhand1 = open(textfile)
wholefile = ""
startposition = 0

header = "number|text|\n"
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

        outputtext = outputtext + str(i-1) + "|" + section + "|\n"
        startposition = endposition
        i += 1
        print (i, len(section))

    else:
        print ("skipped", i, startposition, wholefile[startposition:100]) 
        i +=1

        with open('wigston.csv', 'w') as f:
            f.write(outputtext)
        
        exit()

    #print (outputtext)

print ("complete")

with open('wigston.csv', 'w') as f:
    f.write(outputtext)