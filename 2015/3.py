def execute(puzzle_input):
    x, y = 0, 0
    houses = {(x, y)}
    for move in puzzle_input:
        if move == "^":
            x += 1
        elif move == "v":
            x -= 1
        elif move == ">":
            y += 1
        elif move == "<":
            y -= 1
        houses.add((x, y))
    return houses


def execute1(puzzle_input):
    return len(execute(puzzle_input))


def execute2(puzzle_input):
    santa_instructions = [
        move for pos, move in enumerate(puzzle_input) if pos % 2 == 0
    ]
    robo_instructions = [
        move for pos, move in enumerate(puzzle_input) if pos % 2 == 1
    ]
    return len(execute(santa_instructions) | execute(robo_instructions))
