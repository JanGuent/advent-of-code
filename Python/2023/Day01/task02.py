file = open("input.txt")
sum = 0

for currentline in file:
    first=0
    last=0
    fidx = 0
    lidx = 0
    numbers = {
        'one' : 0,
        'two' : 0,
        'three' : 0,
        'four' : 0,
        'five' : 0,
        'six' : 0,
        'seven' : 0,
        'eight' : 0,
        'nine' : 0
    }
    # Finding the part of the string where each number written as a word has been found first
    for key in numbers:
        numbers[key] = currentline.find(key)


    numberslast = {
        'one' : 0,
        'two' : 0,
        'three' : 0,
        'four' : 0,
        'five' : 0,
        'six' : 0,
        'seven' : 0,
        'eight' : 0,
        'nine' : 0
    }
    # Finding the part of the string where each number written as a word has been found last
    for key in numberslast:
        numberslast[key] = currentline.rfind(key)
  
    #finding and saving the first and last time a number has been found in the string
    currid = 0
    for char in currentline: 
        if char.isnumeric():
            if(first==0):
                first=char
                fidx = currid
                last = char
                lidx = currid
            else:
                last = char
                lidx = currid
        currid = currid+1
 
    for key in numbers:
        #Replacing the first number(numeral) found with a number(word) if it has been found at an earlier stage in the String. Find method returns -1 if subtr has not been found
        if(numbers[key]<fidx and numbers[key]!=-1):
            first=key
            fidx=numbers[key]
        if(numberslast[key]>lidx):
            #Doing the same for the last. Dont have to check if idx is -1 since the id will always be at least 0 and -1 is smaller
            last = key
            lidx = numberslast[key]
    #Converting number(word) into an actual numeral   
    help_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    if(first in help_dict):
        first = help_dict[first]
    if(last in help_dict):
        last = help_dict[last]
    #Concatenating the final first and last numbers and adding to the overall sum
    res = str(first)+str(last)
    sum = sum + int(res)

print(sum)