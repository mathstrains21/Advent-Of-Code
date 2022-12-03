from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    presents = input_file.readlines()
    square_feet = 0
    for present in presents:
        l, w, h = [int(dimension) for dimension in present.split("x")]
        sides = [l * w, l * h, w * h]
        square_feet += sum([2 * side for side in sides]) + min(sides)
    return square_feet



def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    presents = input_file.readlines()
    feet = 0
    for present in presents:
        l, w, h = [int(dimension) for dimension in present.split("x")]
        feet += min([2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h]) + l * w * h
    return feet
