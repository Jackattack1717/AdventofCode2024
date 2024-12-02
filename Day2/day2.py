#!/bin/python3

#read input file and put a report in each element of a list
allreports=[]
input = open("input.txt","r")
for line in input:
   x = line.split(" ")
   y = [int(i) for i in x] # converts the split array into an array of ints
   allreports.append(y)
input.close()

#level check returns -1 if safe, otherwise value is problem val
def levelcheck(n):
    increasing=0 #starts as 0, 1 if increasing, -1 if decreasing
    safe=True
    for i in range(0,len(n)-1):
        x = n[i+1] - n[i]
        #checks changes greater than 3
        if (abs(x) > 3) or (abs(x) == 0):
            #print("change greater than 3 or no change")
            return i
        #establishes if increasing or decreasing
        if increasing == 0:
            if x>0:
                increasing=1
            elif x<0:
                increasing=-1
        #check change in increase or decrease
        if increasing == 1 and x<0:
            #print("went from increase to decrease")
            return i
        if increasing == -1 and x>0:
            #print("went from decrease to increase")
            return i
    return -1

#calculating report safety levels (Challenge pt1)
norm_safetyscore = 0
for report1 in allreports:
    if levelcheck(report1)==-1:
        norm_safetyscore+=1
print("The Safety Score is: " + str(norm_safetyscore))

#Calculate safety score with Problem Dampener(Challenge pt2)
#checks each report, if the report fails initially, it goes through each element to see if an element removed will work
PD_safetyscore = 0
for report2 in allreports:
    i = levelcheck(report2)
    if i != -1:
        for j in range(0,len(report2)):
            currtry=report2.copy() #.copy() makes sure you're passing a shallow copy
            currtry.pop(j)
            if levelcheck(currtry) == -1:
                PD_safetyscore +=1
                break
    else:
        PD_safetyscore +=1

print("The safety score with the Problem Dampener is: " + str(PD_safetyscore))

