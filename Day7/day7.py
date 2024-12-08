#!/bin/python3
from itertools import product
#importing cartesian product to include the new operator for part 2

#read file, put in a list where the first element is the answer num and the second element is a list of operands
calib=[]
f = open("input.txt","r")
for line in f:
    n=line.replace("\n","").split(":")
    n[0]=int(n[0])
    n[1]=n[1].lstrip().split()
    calib.append(n)
f.close()

#create a list of operators
plus='+'
mult='*'
concat='||'
operators=[plus,mult,concat]

#gets every possible combo of + and * operators
def getallcombos(size):
    formatter=("0"+str(size)+"b")
    allcombos=[]
    for i in range(2**size):
        n=format(i,formatter)
        s=[]
        for j in n:
            s.append(operators[int(j)])
        allcombos.append(s)
    return allcombos

#creates an equation with a list of numbers and corresponding array of operators
def getequation(nums,signs):
    equation=[]
    for i,sign in enumerate(signs):
        equation.append(str(nums[i]))
        equation.append(sign)
    equation.append(str(nums[len(nums)-1]))
    return equation

#creates all possible combos of operators, makes an equation using each one, and then runs the evaluator
def evaluateallcombos(equat):
    testi = getallcombos(len(equat)-1)
    answers=[]
    for test in testi:
        g=getequation(equat,test)
        solveequation(g)
        answers.append(solveequation(g))
    return answers

#evaluator to solve an equation perfectly left to right
def solveequation(equation):
    total=int(equation[0])
    for i in range(1,len(equation),2):
        if equation[i]=="+":
            total+=int(equation[i+1])
        if equation[i]=="*":
            total*=int(equation[i+1])
        if equation[i]=="||":
            total=int(str(total)+str(equation[i+1]))
    return(total)

#creates an equation for each calibration number
#if the calibration number exists in the possible answers, add that calib number to the total
totalcalib=0
for i in range(len(calib)):
    n=evaluateallcombos(calib[i][1])
    if n.count(calib[i][0]) >0:
        totalcalib+=calib[i][0]
print("Solution to question 1 is: ",totalcalib)


def newgetallcombos(size):
    l = list(product(operators,repeat=size))
    return l

def newevaluateallcombos(equat):
    testi = newgetallcombos(len(equat)-1)
    answers=[]
    for test in testi:
        g=getequation(equat,test)
        solveequation(g)
        answers.append(solveequation(g))
    return answers

totalcalib1=0
for i in range(len(calib)):
    n=newevaluateallcombos(calib[i][1])
    if n.count(calib[i][0]) >0:
        totalcalib1+=calib[i][0]
print("Solution to question 2 is: ",totalcalib1)
