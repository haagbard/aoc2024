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
    count = 0
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

def get_list_offset(line, line_no):
    return_list = []
    for i in range(len(line)):
        if i != line_no:
            return_list.append(line[i])
    return return_list

def run_dampener(line):
    if all_increase_or_decrease(line):
        all_good = True
        for index in range(0,len(line) - 1):
            val = int(line[index])
            r_val = int(line[index + 1])
            if not check_in_range(r_val, val):
                all_good = False
        if all_good:
            return True
    for i in range(len(line)):
        new_line = get_list_offset(line, i)
        if all_increase_or_decrease(new_line):
            all_good = True
            for index in range(0,len(new_line) - 1):
                val = int(new_line[index])
                r_val = int(new_line[index + 1])
                if not check_in_range(r_val, val):
                    all_good = False
            if all_good:
                return True
    return False

p = []

for line in lines:
    p.append(line.split())

sum = 0

for line in p:
    safe = run_dampener(line)
    if safe:
        sum += 1

print(sum)