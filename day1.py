

with open("./data/day1.txt", "r") as scan_results:
    
    contents = [int(x) for x in scan_results]
    
    # Part 1
    count_part1 = 0
    for i in range(len(contents)):
         if contents[i-1] < contents[i]:
             count_part1 += 1
    
    print(f'Part1: {count_part1}')

    # Part 2
    count_part2 = 0
    for i in range(len(contents)):
        if sum(contents[i:i+3]) < sum(contents[i+1:i+4]):
            count_part2 += 1

    print(f'Part2: {count_part2}')
