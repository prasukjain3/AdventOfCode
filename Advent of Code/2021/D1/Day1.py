#2021
#Day1 Problem 1

with open("AOC D1.txt", 'r') as inputs:
    lines = inputs.readlines()
    numbers = [int(entry.strip()) for entry in lines]
count1 = sum(
    numbers[i] > numbers[i-1]
    for i in range(1,len(numbers))
)

'''
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        count+=1
'''
'''
prev = numbers[0]
for n in numbers[1:]:
    if n > prev:
        count +=1
    prev = n
'''
print("Part 1: ", count1)

#Day1 problem 2
count2 = sum(
    numbers[i] > numbers[i-3]
    for i in range(3, len(numbers))
)
print("Part 2: ", count2)