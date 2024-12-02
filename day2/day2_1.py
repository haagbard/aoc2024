file = 'aoc2024/day2/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

def all_increase(line):
    for index in range(0,len(line) - 1):
        val = int(line[index])
        r_val = int(line[index + 1])
        if val >= r_val:
            return False
    return True

def all_decrease(line):
    for index in range(0,len(line) - 1):
        val = int(line[index])
        r_val = int(line[index + 1])
        if val <= r_val:
            return False
    return True

def all_increase_or_decrease(line):
    return all_increase(line) or all_decrease(line)

def check_in_range(val1, val2):
    abs_sum = abs(val1 - val2)
    if abs_sum <= 0 or abs_sum > 3:
        return False
    return True

p = []

for line in lines:
    p.append(line.split())

sum = 0

for line in p:
    safe = True
    if not all_increase_or_decrease(line):
        safe = False
    else:
        for index in range(0,len(line) - 1):
            val = int(line[index])
            r_val = int(line[index + 1])
            if not check_in_range(r_val, val):
                safe = False
                break
    if safe:
        sum += 1

print(sum)