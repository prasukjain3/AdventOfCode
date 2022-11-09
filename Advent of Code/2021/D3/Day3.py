#2021
#Day3 problem1

with open("AOT D3.txt", "r") as inputs:
    lines = inputs.readlines()
    diagnostic = [entry.strip() for entry in lines]

gamma, epsilon = '', ''
for i in range(len(diagnostic[0])):
    all_entries_at_pos = [entry[i] for entry in diagnostic]
    if all_entries_at_pos.count('0') > len(diagnostic)/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
power_factor = int(gamma, base = 2)*int(epsilon, base = 2)
print(power_factor)

from copy import copy

oxy_diagnostics = copy(diagnostic)
for i in range(len(diagnostic)):
    if len(oxy_diagnostics) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in oxy_diagnostics]
    common_bit = '1' if all_entries_at_pos.count("1") >= len(oxy_diagnostics)/2\
        else '0'
    oxy_diagnostics = [entry for entry in oxy_diagnostics
                       if entry[i] ==common_bit]
oxy_rating = int(oxy_diagnostics[0], base=2)
print("Oxygen ", oxy_diagnostics[0], oxy_rating)


co2_diagnostics = copy(diagnostic)
for i in range(len(diagnostic)):
    if len(co2_diagnostics) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in co2_diagnostics]
    common_bit = '0' if all_entries_at_pos.count("1") >= len(co2_diagnostics)/2\
        else '1'
    co2_diagnostics = [entry for entry in co2_diagnostics
                       if entry[i] ==common_bit]
co2_rating = int(co2_diagnostics[0], base=2)
print("Oxygen ", co2_diagnostics[0], co2_rating)

print("Life Rating: ", oxy_rating*co2_rating)