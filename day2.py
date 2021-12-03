

# Part 1
def calculate_position(coordinates):
    
    horizontal = depth = 0
    for elem in coordinates:
        if elem[0] == 'forward':
            horizontal += elem[1]
        if elem[0] == 'down':
            depth += elem[1]
        if elem[0] == 'up':
            depth -= elem[1]

    return horizontal * depth


# Part 2
def calculate_position_aim(coordinates):
    
    aim = horizontal = depth = 0
    for elem in contents:
        if elem[0] == 'forward':
            horizontal += elem[1]
            depth += aim * elem[1]
        if elem[0] == 'down':
            aim += elem[1]
        if elem[0] == 'up':
            aim -= elem[1]

    return horizontal * depth



with open("./data/day2.txt", "r") as scan_results:
    
    contents = [[int(x) if x.isnumeric() else x for x in line.split()] for line in scan_results]
    
    print(f'Part1: {calculate_position(contents)}')
    print(f'Part2: {calculate_position_aim(contents)}')
