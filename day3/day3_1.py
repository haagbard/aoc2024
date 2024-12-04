import re

def handle_mul(mul):
    group_re = r"mul\((\d+),(\d+)\)"
    val1 = int(re.search(group_re, mul).group(1))
    val2 = int(re.search(group_re, mul).group(2))
    return val1 * val2

file = 'aoc2024/day3/input.txt'

with open(file, 'r') as file:
    all_data = file.read()
    all_data.replace('\n','')

all_mul_re = r"mul\(\d+,\d+\)"

all_mul = re.findall(all_mul_re, all_data)

sum = 0
for mul in all_mul:
    sum += handle_mul(mul)

print(sum)