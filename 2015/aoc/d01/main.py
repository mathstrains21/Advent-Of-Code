from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    floor = 0
    for bracket in input_file.read():
        if bracket == "(":
            floor += 1
        elif bracket == ")":
            floor -= 1
    return floor


def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    floor = 0
    for position, bracket in enumerate(input_file.read()):
        if floor == -1:
            return position
        if bracket == "(":
            floor += 1
        elif bracket == ")":
            floor -= 1
    return None
