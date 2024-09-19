res = 0
file = open("input.txt")

for line in file:
    line = line[5:]
    id = line[:line.find(":")]
    
    line = line[line.find(":")+1:]
    seen = {'red': 0,
            'green': 0,
            'blue': 0}


    splits = line.split(";")

    for round in splits:
        for key in seen:
            if(round.find(key) != -1 and round[round.find(key)-3:round.find(key)].isnumeric()-1):
                val = round[round.find(key)-3:round.find(key)-1]
                seen[key] = max(seen[key],int(val))
                
    power = seen["blue"]*seen["green"]*seen["red"]
    #print("Game: ",id,"Power: ",power)
    res = res + power

print(res)
