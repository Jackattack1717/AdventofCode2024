#!/bin/python3

#Read file with all instructions in inst[] and pages in pages[]
inst=[]
pages=[]
file = open("input.txt","r")
filechange = 0
for line in file:
    f = line.replace("\n","")
    if f == "":
        filechange = 1
    elif filechange == 0:
        inst.append(f.split("|"))
    else:
        pages.append(f.split(","))
file.close()

#returns an array of all the nums that can't come before a given number
def getrules(num):
    rules=[]
    for i in range(0,len(inst)):
        if num == inst[i][0]:
            rules.append(inst[i][1])
    return rules

#returns -1 if follows rules, wrong index if breaks
def checkrules(page,rule,index):
    for i in range(0,index):
        if rule.count(page[i])!=0:
            return i
    return -1

#loops thru the page swapping values according to the rules until the i flag shows no changes were made
def fixupdate(page):
    notfixed = True
    while notfixed:
        i = 0
        for j in range(1,len(page)):
            r = getrules(page[j])
            c = checkrules(page,r,j)
            if not(c==-1):
                i+=1
                temp = page[c]
                page[c] = page[j]
                page[j] = temp
        if i == 0:
            notfixed = False

#cycles thru all the updates in the main array list, checks the rules for each element (minus the first), and returns the total of the center number
total = 0
total2 = 0
for update in pages:
    passflag = True
    for j in range(1,len(update)):
        r = getrules(update[j])
        c = checkrules(update,r,j)
        if not(c==-1): #try to perform 1 swap-fix early for giggles
            temp = update[c]
            update[c] = update[j]
            update[j] = temp
            passflag = False
    if passflag:
        total+=int(update[int(len(update)/2)])
    else:
        fixupdate(update)
        total2+=int(update[int(len(update)/2)])

print("The total for the first question is " + str(total))
print("The total for the second question is " + str(total2))
