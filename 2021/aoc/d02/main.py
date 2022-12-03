from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    instructions = [instruction.split() for instruction in input_file.read().splitlines()]
    distance = 0
    depth = 0

    for i in instructions:
        i[1] = int(i[1])
        if i[0] == "forward":
            distance += i[1]
        elif i[0] == "down":
            depth += i[1]
        elif i[0] == "up":
            depth -= i[1]
    return distance * depth


def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    instructions = [instruction.split() for instruction in input_file.read().splitlines()]
    distance = 0
    depth = 0
    aim = 0

    for i in instructions:
        i[1] = int(i[1])
        if i[0] == "forward":
            distance += i[1]
            depth += aim * i[1]
        elif i[0] == "down":
            aim += i[1]
        elif i[0] == "up":
            aim -= i[1]
    return distance * depth
