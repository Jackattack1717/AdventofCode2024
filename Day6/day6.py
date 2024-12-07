#!/bin/python3

guardmap = []
inputfile = open("testinput.txt","r")
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
def coordadd(x,y):
    result=[0,0]
    result[0]=x[0] + y[0]
    result[1]=x[1] + y[1]
    return result

#print current map for troubleshooting purposes
def printmap(gmap):
    for i in gmap:
        print(i)
    print()

'''
for s in directions:
    print(s)
currspot = guardmap[g[0]][g[1]]
outofbounds = (g[0]<0 or g[0]>len(guardmap)) or (g[1]<0 or g[1]>len(guardmap[g[0]]))
'''

#find guard initial spot and change to an 'X'
g = findguard(guardmap)
guardmap[g[0]][g[1]] = 'X'



nextspot=[]

#traversal 'works', just need to continue the traversal until out of bounds and not fail
def traverse(g,guardmap):
    for move in directions:
        nspot = cooradd(g,move)
        outofbounds = ((nspot[0]<0 or nspot[0]>len(guardmap))or(nspot[1]<0 or nspot[1]>len(guardmap[nspot[0]]))
        if outofbounds:
            return 0
        else:
            if guardmap[nspot[0]][nspot[1]] != '#':
                guardmap[nspot[0]][nspot[1]] = 'X'
                g = nspot
    return 


'''
def traverse(g,guardmap):
    for s in directions:
        outofbounds = (g[0]<0 or g[0]>len(guardmap)) or (g[1]<0 or g[1]>len(guardmap[g[0]]))
        currspot = guardmap[g[0]][g[1]]
        while not(outofbounds) and currspot != '#':
            guardmap[g[0]][g[1]] = 'X'
            nextspot = coordadd(g,s)
            outofbounds = (nextspot[0]<0 or nextspot[0]>len(guardmap)) or (nextspot[1]<0 or nextspot[1]>len(guardmap[nextspot[0]]))
            currspot = guardmap[nextspot[0]][nextspot[1]]
            if not(outofbounds) and currspot != '#':
                g = nextspot
    return g
g=traverse(g,guardmap)
print(g)

for i in guardmap:
    print(i)
print()
'''
