#!/bin/python3

guardmap = []
inputfile = open("input.txt","r")
for line in inputfile:
    guardmap.append(list(line.replace("\n","")))
inputfile.close()
#print(guardmap)

#define all the directions we can move in and put them in a list in the order of the directions the guard can move
up = [-1,0]
down = [1, 0]
left = [0,-1]
right = [0,1]
directions = [up,right,down,left]

#initial function to find where the 'guard' is
def findguard(inmap):
    coords = []
    for i in range(0,len(inmap)):
        for j in range (0,len(inmap[i])):
            if inmap[i][j] == "^":
                coords = list((i,j))
                return coords
    return 0

#helper function to move in a direction
def cooradd(x,y):
    result=[0,0]
    result[0]=x[0] + y[0]
    result[1]=x[1] + y[1]
    return result

#print current map for troubleshooting purposes
def printmap(gmap):
    for i in gmap:
        print(i)
    print()


#traversal traverses the guard thru the maze
#returns g if runs into #
#return 0 if runs into OOB
def traverse(g,guardmap,move):
    outofbounds = False
    nspot = g
    while not(outofbounds):
        if guardmap[nspot[0]][nspot[1]] != '#':
            g=nspot
            guardmap[nspot[0]][nspot[1]] = 'X'
        else:
            #print(g)
            return g
        nspot = cooradd(nspot,move)
        outofbounds = (nspot[0]<0 or nspot[0]>=len(guardmap)) or (nspot[1]<0 or nspot[1]>=len(guardmap[nspot[0]]))
        if outofbounds:
            break
    return 0

#find guard initial spot
g = findguard(guardmap)

while g!=0:
    for go in directions:
        #print(g)
        if g !=0:
            g=traverse(g,guardmap,go)

#printmap(guardmap)

#finds the total number of 'X's
total = 0
for i in range(0,len(guardmap)):
    for j in range(0,len(guardmap[i])):
        if guardmap[i][j]=='X':
            total+=1
print("The solution to puzzle 1 is: " +str(total))
