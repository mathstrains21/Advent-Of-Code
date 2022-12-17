from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    inpt = [[list(map(int, j.split(","))) for j in i.split(" -> ")] for i in input_file.read().strip().split('\n')]

    walls = set()
    sands = set()

    for w in inpt:
        for i in range(len(w) - 1):
            start = w[i]
            end = w[i + 1]

            if start[0] > end[0]:
                for j in range(end[0], start[0] + 1):
                    walls.add((j, end[1]))
            elif start[0] < end[0]:
                for j in range(start[0], end[0] + 1):
                    walls.add((j, start[1]))
            
            if start[1] > end[1]:
                for j in range(end[1], start[1] + 1):
                    walls.add((end[0], j))
            elif start[1] < end[1]:
                for j in range(start[1], end[1] + 1):
                    walls.add((start[0], j))
    
    max_depth = max(map(lambda a: a[1], walls))
    sand_location = (500, 0)

    while sand_location[1] <= max_depth:
        for x, y in ((0,1), (-1, 1), (1, 1)):
            temp = sand_location[0] + x, sand_location[1] + y
            if temp not in walls and temp not in sands:
                sand_location = temp
                break
        else:
            sands.add(sand_location)
            sand_location = (500, 0)
    
    return len(sands)

def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    inpt = [[list(map(int, j.split(","))) for j in i.split(" -> ")] for i in input_file.read().strip().split('\n')]

    walls = set()
    sands = set()

    for w in inpt:
        for i in range(len(w) - 1):
            start = w[i]
            end = w[i + 1]

            if start[0] > end[0]:
                for j in range(end[0], start[0] + 1):
                    walls.add((j, end[1]))
            elif start[0] < end[0]:
                for j in range(start[0], end[0] + 1):
                    walls.add((j, start[1]))
            
            if start[1] > end[1]:
                for j in range(end[1], start[1] + 1):
                    walls.add((end[0], j))
            elif start[1] < end[1]:
                for j in range(start[1], end[1] + 1):
                    walls.add((start[0], j))
    
    max_depth = max(map(lambda a: a[1], walls))
    sand_location = (500, 0)

    while True:
        for x, y in ((0,1), (-1, 1), (1, 1)):
            temp = sand_location[0] + x, sand_location[1] + y
            if temp not in walls and temp not in sands and temp[1] < max_depth + 2:
                sand_location = temp
                break
        else:
            sands.add(sand_location)
            if sand_location == (500, 0):
                break
            sand_location = (500, 0)
    
    return len(sands)
