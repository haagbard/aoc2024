from re import findall
from sys import stdin

file = 'aoc2024/day3/input.txt'

with open(file, 'r') as file:
    data = file.read()
    data.replace('\n','')

data.replace('\n','')


# part 1
def calc(code: str) -> int:
    pattern = r'mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)'
    return sum(int(a) * int(b) for a, b in findall(pattern, code))


print(calc(data))

# part 2
doos = [do.split("don't()")[0] for do in data.split('do()')]
print(calc(''.join(doos)))