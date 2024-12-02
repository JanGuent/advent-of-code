import itertools
testlines = open("aoc/advent-of-code/Python/2024/Day02/test.txt").read().splitlines()
lines = open("aoc/advent-of-code/Python/2024/Day02/input.txt").read().splitlines()
#Instantly turn textfile into lines of ints
lines = [list(map(int,line.split()))for line in lines]
testlines = [list(map(int,line.split()))for line in testlines]


def checkallDesc(l:list[int])->bool:
    for a , b in itertools.pairwise(l):
        if a <= b:
            return False
    return True
def checkAllAsc(l:list[int])->bool:
    for a , b in itertools.pairwise(l):
        if a >= b:
            return False
    return True

def checkValidSteps(l:list[int])->bool:
    for a,b in itertools.pairwise(l):
        if abs(b-a)>3:
            return False
    return True

def checkValidLine(line:list[int])->bool:
    if checkAllAsc(line) or checkallDesc(line):
        if(checkValidSteps(line)):
            return True
    return False
            
def Task01Solve(lineslist) -> int:
    res = 0
    for line in lineslist:
        if checkAllAsc(line) or checkallDesc(line):
            if(checkValidSteps(line)):
                res +=1
                
    return res
#Ceck if line is valid for every variation of the line with one removed.
def Task02Solve(lineslist)-> int:
    res =0
    for line in lineslist:
        if not checkValidLine(line):
            for i in range(len(line)):
                oneRemoved = list(line)
                oneRemoved.pop(i)
                if(checkValidLine(oneRemoved)):
                    res +=1
                    break
        else:
            res+=1
    return res


print(Task01Solve(lines))
print(Task02Solve(lines))