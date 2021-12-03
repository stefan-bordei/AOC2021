
# Helper functions
def get_most_common(arr):
    return max(set(arr), key = arr.count)


def get_least_common(arr):
    return min(set(arr), key = arr.count)


def check_equal(arr):
    return arr.count('0') == arr.count('1')


def to_decimal(num):
    return int(num, 2)


# Part 1
def calculate_power_consumption(inp):
    
    gamma = epsilon = ''
    for i in range(len(inp[0])):
        gamma += get_most_common([x[i] for x in inp])
        epsilon += get_least_common([x[i] for x in inp])

    return to_decimal(gamma) * to_decimal(epsilon)


# Part 2
def calculate_life_support_rating(inp):
    
    o2 = co2 = inp
    while len(o2) != 1 and len(o2) == len(co2):
        for i in range(len(inp[0])):
            
            o2_temp = co2_temp = []
            if check_equal([x[i] for x in o2]):
                o2_temp = [x for x in o2 if x[i] == '1']
            else:
                o2_temp = [x for x in o2 if x[i] == get_most_common([x[i] for x in o2])]
            
            if check_equal([x[i] for x in co2]):
                co2_temp = [x for x in co2 if x[i] == '0']
            else:
                co2_temp = [x for x in co2 if x[i] == get_least_common([x[i] for x in co2])]
            
            o2, co2 = o2_temp, co2_temp

    return to_decimal(o2[0]) * to_decimal(co2[0])

with open("./data/day3.txt", "r") as scan_results:
    
    contents = [line.strip() for line in scan_results]
    print(f'Part2: {calculate_life_support_rating(contents)}')
    print(f'Part1: {calculate_power_consumption(contents)}')
