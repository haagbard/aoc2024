import re

file = 'aoc2024/day5/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

updates_re = r"(\d+)\|(\d+)"

updates = []
prints_lines = []

for line in lines:
    if re.match(updates_re, line):
        s = re.search(updates_re, line)
        updates.append((s.group(1), s.group(2)))
    elif line.rstrip() != '':
        prints_lines.append(line)

def find_middle_value(prints):
    middleIndex = int((len(prints) - 1)/2)
    return int(prints[middleIndex])

def is_valid(prints):
    seen = set()
    for value in prints:
        seen.add(value)

        for a, b in updates:
            if a in seen and b in seen:
                if prints.index(b) < prints.index(a):
                    return False
    return True

def reorder(prints):
    seen = set()
    for value in prints:
        seen.add(value)

        for a, b in updates:
            if a in seen and b in seen:
                if prints.index(b) < prints.index(a):
                    b_index = prints.index(b)
                    prints.remove(a)
                    prints.insert(b_index, a)
    return prints

sum = 0

for print_line in prints_lines:
    prints = print_line.split(',')
    success = is_valid(prints)
    
    if success == False:
        prints = reorder(prints)
        middle = find_middle_value(prints)
        sum += middle

print(sum)