#2021
#Day3 problem1

with open("AOT D3.txt", "r") as inputs:
    lines = inputs.readlines()
    numbers = [entry.strip() for entry in lines]

gamma, epsilon = '', ''
for i in range(len(numbers[0])):
    all_entries_at_pos = [entry[i] for entry in numbers]
    if all_entries_at_pos.count('0') > len(numbers)/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
power_factor = int(gamma, base = 2)*int(epsilon, base = 2)
print(power_factor)
