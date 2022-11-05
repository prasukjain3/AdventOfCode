#2021
#Day2 Problem2

with open("AOC D2.txt", "r") as inputs:
    lines = inputs.readlines()
    numbers = [entry.strip() for entry in lines]

hp, depth, aim = 0, 0, 0
for i in numbers:
    direction, amount = i.split(' ')[0], int(i.split(' ')[1])
    if 'forward' in direction:
        hp += amount
        depth += aim*amount
    elif 'up' in direction:
        aim -= amount
    elif 'down' in direction:
        aim += amount
print(hp*depth)
