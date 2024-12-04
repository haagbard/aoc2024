import re

def handle_mul(mul):
    group_re = r"mul\((\d+),(\d+)\)"
    val1 = int(re.search(group_re, mul).group(1))
    val2 = int(re.search(group_re, mul).group(2))
    return val1 * val2

def get_substring(all_data, dos, donts):
    ret_str = ''
    for i in range(0,len(dos)):
        do_pos = dos[i]
        dont_pos = donts[i]
        ret_str += all_data[do_pos:dont_pos]
    return ret_str

file = 'aoc2024/day3/input.txt'

with open(file, 'r') as file:
    all_data = file.read()
    all_data.replace('\n','')

all_data.replace('\n','')

all_mul_re = r"mul\(\d+,\d+\)"

dos_split = all_data.split("do()")

all_data_lines = []

for dos in dos_split:
    dont_split = dos.split("don't()")
    all_data_lines.append(dont_split[0])

sum = 0

for line in all_data_lines:
    all_mul = re.findall(all_mul_re, line)

    for mul in all_mul:
        sum += handle_mul(mul)

print(sum)