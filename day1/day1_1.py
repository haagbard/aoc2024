file = 'aoc2024/day1/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

l_list = []
r_list = []

for line in lines:
    p = line.split()
    l_list.append(int(p[0]))
    r_list.append(int(p[1]))

l_list.sort()
r_list.sort()

sum = 0

for index, l_val in enumerate(l_list):
    r_val = r_list[index]
    sum += abs(r_val - l_val)

print(sum)