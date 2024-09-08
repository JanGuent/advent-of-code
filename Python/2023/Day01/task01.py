file = open("input.txt")
sum = 0        
for currentline in file:
    first = 0
    last = 0
    for char in currentline: 
        if char.isnumeric():
            if(first==0):
                first=char
                last = char
            else:
                last = char

    res = str(first) + str(last)
    sum = sum + int(res)
    
print(sum)