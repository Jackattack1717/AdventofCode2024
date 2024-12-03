#!/bin/python3

import re

allmuls = []
#regex the file for all instances where mul(number,number) happens and store it in a list variable allmuls
fileinput = open("input.txt","r")
for line in fileinput:
    #vals = re.findall(r"mul\(\d+,\d+\)",line)
    vals = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)",line)
    allmuls += vals

#function to take each string, isolate the 2 numbers, multiply them together, and return the result
def mulfunc(stringinput):
    inputstr=stringinput.split(',')
    x=int(inputstr[0].replace("mul(",""))
    y=int(inputstr[1].replace(")",""))
    return x*y

result1=0
for muls in allmuls:
    if muls!="do()" and muls!="don't()":
        result1+=mulfunc(muls)
print("Results for the first part is: " + str(result1))

result2=0
dontrun=0
for muls in allmuls:
    if muls=="do()":
        dontrun=0
    if muls=="don't()":
        dontrun=1
    if dontrun==0 and muls!="do()" and muls!="don't":
        result2+=mulfunc(muls)

print("Results for the second part is: " + str(result2))
