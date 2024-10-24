from collections import defaultdict
lines = open("advent-of-code/Python/2023/Day04/input.txt").read().splitlines()
def part01():
    sol = 0
    hits_on_each_card = defaultdict()
    for card, line in enumerate(lines): 
        line = line[line.find(":")+2:]
        winning_numbers_str = line[:line.find("|")]
        winning_numbers = [int(ele) for ele in winning_numbers_str.split()]
        my_numbers_str = line[line.find("|")+2:]
        my_numbers = [int(el) for el in my_numbers_str.split()]
        matches = 0
        for num in my_numbers:
            if(num in winning_numbers):
                matches+=1
        hits_on_each_card[card] = matches
    for num in hits_on_each_card:
        if(hits_on_each_card[num]>0):
            exponent = hits_on_each_card[num]-1
            sol += 2**exponent
    print(sol)

def part02():
    sol = 0
    number_of_each_card = defaultdict()
    for init in range(len(lines)):
        number_of_each_card[init] = 1
    for card, line in enumerate(lines): 
        line = line[line.find(":")+2:]
        winning_numbers_str = line[:line.find("|")]
        winning_numbers = [int(ele) for ele in winning_numbers_str.split()]
        my_numbers_str = line[line.find("|")+2:]
        my_numbers = [int(el) for el in my_numbers_str.split()]
        matches = 0
        for num in my_numbers:
            if(num in winning_numbers):
                matches+=1
        for nex in range(matches):
            factor  = 1 * number_of_each_card[card]
            number_of_each_card[card+nex+1] +=factor
    for sum in number_of_each_card:
        sol += number_of_each_card[sum]
    print(sol)

part01()
part02()

test = 0
