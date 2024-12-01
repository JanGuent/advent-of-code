from collections import Counter
testlines = open("test.txt").read().splitlines()
lines = open("input.txt").read().splitlines()

def Task01Solve(lineslist) -> int:
    dist = 0
    leftList = []
    rightList=[]
    #Split file in two sorted lists in order to compare them later
    for line in lineslist:
        leftList.append(int(line.split()[0]))
        rightList.append(int(line.split()[1]))
        leftList.sort()
        rightList.sort()
    #Compare which element is larger and add diff to final distance
    for idx, ele in enumerate(leftList):
        if(rightList[idx] >= ele):
            dist += rightList[idx] -ele
        else:
            dist += ele - rightList[idx] 
    return dist
    
def Task02Solve(lineslist)-> int:
    res =0
    leftList = []
    rightList=[]
    #Split file in two sorted lists in order to compare them later
    for line in lineslist:
        leftList.append(int(line.split()[0]))
        rightList.append(int(line.split()[1]))
    #Count how often each element from the left list in right list 
    for num in leftList:
        factor =0
        for check in rightList:
            if num == check:
                factor+=1
        res += num * factor
    return res

def Task02SolveDifferent(lineslist) -> int:
    res =0
    leftList = []
    rightList=[]
    #Split file in two sorted lists in order to compare them later
    for line in lineslist:
        leftList.append(int(line.split()[0]))
        rightList.append(int(line.split()[1]))
    #Get count using Counter and add correct values to res
    count = Counter(rightList)
    for num in leftList:
        if num in count:
            res += num * count[num]
    return res
print(Task01Solve(lines))
print(Task02Solve(lines))
print(Task02SolveDifferent(lines))
