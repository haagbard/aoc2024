file = 'aoc2024/day4/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

max_x = len(lines[0])
max_y = len(lines)

# X, Y
directions = {'NE': (1, -1), 'SE': (1, 1), 'SW': (-1, 1), 'NW': (-1, -1)}

def check_bounds(x, y):
    if x < 0 or x >= max_x:
        return False
    if y < 0 or y >= max_y:
        return False
    return True

def check_valid_next(char):
    if char == 'M':
        return 'A'
    elif char == 'A':
        return 'S'
    return None

def next_move(x, y, direction): 
    step_x, step_y = directions[direction]
    next_x = x + step_x
    next_y = y + step_y
    return next_x, next_y

def check_next(char, x, y, direction):
    next_x, next_y = next_move(x, y, direction)
    if check_bounds(next_x, next_y):
        valid_next_char = check_valid_next(char)
        next_char = lines[next_y][next_x]
        if next_char == valid_next_char:
            if next_char == 'S':
                return True
            return check_next(next_char, next_x, next_y, direction)
    return False

sum = 0

counter = 0
mas_dict = {}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'M':
            for direction in directions:
                success = check_next(char, x, y, direction)
                if success:
                    a_pos_x, a_pos_y = next_move(x, y, direction)
                    mas_dict[counter] = [a_pos_x, a_pos_y]
                    counter += 1

for c in mas_dict:
    tmp_dict = {}
    for c_tmp in mas_dict:
        if c != c_tmp:
            tmp_dict[c_tmp] = mas_dict[c_tmp]
    val = mas_dict[c]
    if val in tmp_dict.values():
        sum += 1

sum = int(sum / 2)

print(sum)