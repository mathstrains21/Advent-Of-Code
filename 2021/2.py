def execute1(puzzle_input):
    instructions = [instruction.split() for instruction in puzzle_input.splitlines()]
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


def execute2(puzzle_input):
    instructions = [instruction.split() for instruction in puzzle_input.splitlines()]
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
