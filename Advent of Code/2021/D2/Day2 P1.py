#2021
#Day2 Problem1

with open("AOC D2 P1.txt", "r") as inputs:
    lines = inputs.readlines()
    numbers = [entry.strip() for entry in lines]

x = 0
y = 0
for i in numbers:
    direction, amount = i.split(' ')[0], int(i.split(' ')[1])
    if 'forward' in direction:
        x += amount
    elif 'down' in direction:
        y += amount
    elif 'up' in direction:
        y -= amount
print(x*y)