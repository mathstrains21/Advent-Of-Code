from typing import IO


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


def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    return len(execute(input_file.read()))



def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    instructions = list(input_file.read())
    santa_instructions = instructions[0::2]
    robo_instructions = instructions[1::2]
    return len(execute(santa_instructions) | execute(robo_instructions))
