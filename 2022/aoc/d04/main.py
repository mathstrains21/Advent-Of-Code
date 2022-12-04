from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    pairs = input_file.read().splitlines()
    total = 0
    for pair in pairs:
        e1, e2 = pair.split(",")
        e1 = e1.split("-")
        e2 = e2.split("-")

        e1min = int(e1[0])
        e1max = int(e1[1])
        e2min = int(e2[0])
        e2max = int(e2[1])

        e1nums = set(range(e1min, e1max + 1))
        e2nums = set(range(e2min, e2max + 1))

        if e1nums >= e2nums or e2nums >= e1nums:
            total += 1
    return total


def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    pairs = input_file.read().splitlines()
    total = 0
    for pair in pairs:
        e1, e2 = pair.split(",")
        e1 = e1.split("-")
        e2 = e2.split("-")

        e1min = int(e1[0])
        e1max = int(e1[1])
        e2min = int(e2[0])
        e2max = int(e2[1])

        e1nums = set(range(e1min, e1max + 1))
        e2nums = set(range(e2min, e2max + 1))

        if len(e1nums & e2nums) != 0:
            total += 1
    return total
