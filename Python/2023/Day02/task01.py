#Accidentally misunderstood the task and checked for games which wouldve been possible if the shown cubes were kept out of the bag after showing

res = 0
file = open("input.txt")

for line in file:
    line = line[5:]
    success = True
    id = line[:line.find(":")]
    
    line = line[line.find(":")+1:]
    seen = {'red': 0,
            'green': 0,
            'blue': 0}


    splits = line.split(";")

    for round in splits:
        #print(round)
        for key in seen:
            if(round.find(key) != -1 and round[round.find(key)-3:round.find(key)].isnumeric()-1):
                #print(round[round.find(key)-3:round.find(key)-1])
                val = round[round.find(key)-3:round.find(key)-1]
                #print("Key: ",key,"Value:",val)
                seen[key] = seen[key] + int(val)

    #print(seen)
    if(seen["red"]>12 or seen["green"]>13 or seen["blue"]>13):
        success = False
    if(success):
        print("Success added, ID= ", id)
        res = res+int(id)

print(res)

    
    
    
    

# val = line[:line.find(" ")]
# print("Val = ", val)
# line = line[line.find(" ")+1:]
# print(line)
# while(len(line>1)):
#     val = line[:line.find(" ")]
 