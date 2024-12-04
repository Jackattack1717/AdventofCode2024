#!/bin/python3

wordsearch=[]
file=open("input.txt","r")
for line in file:
   line=line.replace("\n","")
   wordsearch.append(list(line))

def matrixsearch1(array,dir1,dir2):
    result1=0
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if (i+(3*dir1))>=0 and (i+(3*dir1))<=len(array)-1 and (j+(3*dir2)>=0) and (j+(3*dir2)<=len(array[i])-1): 
                if array[i][j]=="X":
                    if array[i+dir1][j+dir2]=="M":
                        if array[i+(2*dir1)][j+(2*dir2)]=="A":
                            if array[i+(3*dir1)][j+(3*dir2)]=="S":
                                result1+=1
    return result1

def matrixsearch2(array):
    result2=0
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if(i-1)>=0 and (i+1)<=len(array)-1 and (j-1)>=0 and (j+1)<=len(array)-1:
                if array[i][j]=="A":
                    leftdiag_ms=(array[i-1][j+1]=="M" and array[i+1][j-1]=="S")
                    leftdiag_sm=(array[i+1][j-1]=="M" and array[i-1][j+1]=="S")
                    rightdiag_ms=(array[i-1][j-1]=="M" and array[i+1][j+1]=="S")
                    rightdiag_sm=(array[i+1][j+1]=="M" and array[i-1][j-1]=="S")
                    if (leftdiag_ms or leftdiag_sm) and (rightdiag_ms or rightdiag_sm):
                        result2+=1
    return result2

total1 = 0
for i in range(-1,2):
    for j in range(-1,2):
        if not(i==0 and j==0):
            total1+=matrixsearch1(wordsearch,i,j)
print("The solution to the XMAS crossword is: "+ str(total1))

total2=matrixsearch2(wordsearch)
print("The solution to the X-MAS crossword is: " + str(total2))
