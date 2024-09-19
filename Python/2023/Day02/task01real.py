res = 0
file = open("input.txt")

for line in file:
    line = line[5:]
    success = True
    id = line[:line.find(":")]
    
    line = line[line.find(":")+1:]
    seen = {'red': 12,
            'green': 13,
            'blue': 14}


    splits = line.split(";")

    for round in splits:
        #print(round)
        for key in seen:
            if(round.find(key) != -1 and round[round.find(key)-3:round.find(key)].isnumeric()-1):
                #print(round[round.find(key)-3:round.find(key)-1])
                val = round[round.find(key)-3:round.find(key)-1]
                if(int(val)>seen[key]):
                    success = False
                    break
    
    if(success):
        print("Success added, ID= ", id)
        res = res+int(id)

print(res)
