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

def execute1(puzzle_input):
    return max(execute(puzzle_input.splitlines()))

def execute2(puzzle_input):
    elves = execute(puzzle_input.splitlines())
    cals = 0
    for _ in range(3):
        elf = max(elves)
        cals += elf
        elves.remove(elf)
    return cals