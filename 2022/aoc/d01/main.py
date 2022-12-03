from typing import IO


def execute(data):
    elves = []
    elf = 0

    for line in data:
        try:
            elf += int(line)
        except ValueError:
            elves.append(elf)
            elf = 0
    return elves


def p_1(input_file: IO, debug=False):  # pylint: disable=unused-argument
    return max(execute(input_file.read().splitlines()))


def p_2(input_file: IO, debug=False):  # pylint: disable=unused-argument
    elves = execute(input_file.read().splitlines())
    cals = 0
    for _ in range(3):
        elf = max(elves)
        cals += elf
        elves.remove(elf)
    return cals
