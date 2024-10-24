from collections import defaultdict
from dataclasses import dataclass
@dataclass
class coordinate:
    x: int
    y: int
lines = open("advent-of-code/Python/2023/Day03/input.txt").read().splitlines()


def is_symbol(char: str) -> bool:
    return char != "." and not char.isdigit()

def get_symbol_coordinates()->list:
    pos = list()
    for y , line in enumerate(lines):
        for x, cell in enumerate(line):
            if is_symbol(cell):
                pos.append(coordinate(x,y))
    return pos
    
    
def part01():
    positions = get_symbol_coordinates()
    startNums = set()
    for pos in positions:
        lines[pos.y][pos.x]
        for cr in [pos.y-1,pos.y,pos.y+1]:
            for cc in [pos.x-1,pos.x,pos.x+1]:
                if cr <0 or cr >= len(lines) or cc <0 or cc >= len(lines[cr]) or not lines[cr][cc].isdigit():
                    continue
                while cc > 0 and lines[cr][cc-1].isdigit():
                    cc-=1
                startNums.add((cr,cc))
    ns = []
    for yc, xc in startNums:
        s = ""
        while xc <len(lines[yc]) and lines[yc][xc].isdigit():
            s+= lines[yc][xc]
            xc+=1
        ns.append(int(s))
    print(sum(ns))

def part02():
    total = 0
    positions = get_symbol_coordinates()
    
    for pos in positions:
        lines[pos.y][pos.x]
        startNums = set()
        for cr in [pos.y-1,pos.y,pos.y+1]:
            for cc in [pos.x-1,pos.x,pos.x+1]:
                if cr <0 or cr >= len(lines) or cc <0 or cc >= len(lines[cr]) or not lines[cr][cc].isdigit():
                    continue
                while cc > 0 and lines[cr][cc-1].isdigit():
                    cc-=1
                startNums.add((cr,cc))
        if(len(startNums)!=2):
            continue
        ns = []
        for yc, xc in startNums:
            s = ""
            while xc <len(lines[yc]) and lines[yc][xc].isdigit():
                s+= lines[yc][xc]
                xc+=1
            ns.append(int(s)) 
        total += ns[0]*ns[1]
    print(total)        
                
part01()
part02()