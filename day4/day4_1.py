file = 'aoc2024/day4/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

max_x = len(lines[0])
max_y = len(lines)

# X, Y
directions = {'N':(0, -1), 'NE': (1, -1), 'E': (1, 0), 'SE': (1, 1), 'S': (0, 1), 'SW': (-1, 1), 'W': (-1, 0), 'NW': (-1, -1)}

def check_bounds(x, y):
    if x < 0 or x >= max_x:
        return False
    if y < 0 or y >= max_y:
        return False
    return True

def check_valid_next(char):
    if char == 'X':
        return 'M'
    elif char == 'M':
        return 'A'
    elif char == 'A':
        return 'S'
    return None

def check_next(char, x, y, direction):
    step_x, step_y = directions[direction]
    next_x = x + step_x
    next_y = y + step_y
    if check_bounds(next_x, next_y):
        valid_next_char = check_valid_next(char)
        next_char = lines[next_y][next_x]
        if next_char == valid_next_char:
            if next_char == 'S':
                return True
            return check_next(next_char, next_x, next_y, direction)
    return False

sum = 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'X':
            for direction in directions:
                success = check_next(char, x, y, direction)
                if success:
                    sum += 1

print(sum)