def execute1(puzzle_input):
    floor = 0
    for bracket in puzzle_input:
        if bracket == "(":
            floor += 1
        elif bracket == ")":
            floor -= 1
    return floor


def execute2(puzzle_input):
    floor = 0
    for position, bracket in enumerate(puzzle_input):
        if floor == -1:
            return position
        if bracket == "(":
            floor += 1
        elif bracket == ")":
            floor -= 1
