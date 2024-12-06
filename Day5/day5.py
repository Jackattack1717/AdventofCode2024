#!/bin/python3

printinstructions=[]
file = open("testinput.txt","r")
for line in file:
    printinstructions.append(line.replace("\n",""))
print(printinstructions)
