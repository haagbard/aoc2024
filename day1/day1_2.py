file = 'aoc2024/day1/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

l_list = []
r_list = []

for line in lines:
    p = line.split()
    l_list.append(int(p[0]))
    r_list.append(int(p[1]))

sum = 0

for l_val in l_list:
    c = r_list.count(l_val)
    sum += l_val * c

print(sum)