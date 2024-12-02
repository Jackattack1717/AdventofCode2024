#!/bin/python3
list1 = []
list2 = []
allvalues = []
input = open("input.txt","r")
for line in input:
   x = line.split("   ")
   list1.append(int(x[0]))
   list2.append(int(x[1]))

list1.sort()
list2.sort()

#calculating total distance
total = 0
for i in range(0,len(list1)):
    total += abs(list1[i]-list2[i])
print("The distance between the 2 lists is: " + str(total))

#calculate similarity score
similarityscore = 0
for i in list1:
    similarityscore += i * list2.count(i)
print("similarity score is: " + str(similarityscore))
