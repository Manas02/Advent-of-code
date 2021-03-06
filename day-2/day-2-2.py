from operator import xor

with open("input.txt") as f:
    data = f.read().splitlines() 

def day2_2(data):
    count = 0
    for line in data:
        if xor(line.split(" ")[2][int(line.split(" ")[0].split('-')[0]) - 1] == line.split(" ")[1][0], line.split(" ")[2][int(line.split(" ")[0].split('-')[1]) - 1] == line.split(" ")[1][0]):
            count += 1
    
    print(count)

day2_2(data)
