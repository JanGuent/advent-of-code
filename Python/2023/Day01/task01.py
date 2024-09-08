#Finding first and last number in a string taken from a textfile. Taken from Advent of Code
file = open("input.txt")
sum = 0        
for currentline in file:
    first = 0
    last = 0
    for char in currentline: 
        if char.isnumeric():
            #If a number is first found it is set as both first and last to account for there possibly only being one number
            if(first==0):
                first=char
                last = char
            else:
                #If first is not 0, a number has already been found before and we only update the last variable
                last = char
    #Concatenating the number and adding it to the overall sum
    res = str(first) + str(last)
    sum = sum + int(res)
    
print(sum)