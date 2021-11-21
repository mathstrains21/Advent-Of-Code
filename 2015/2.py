def execute1(puzzle_input):
    presents = puzzle_input.splitlines()
    square_feet = 0
    for present in presents:
        l, w, h = [int(dimension) for dimension in present.split('x')]
        sides = [l * w, l * h, w * h]
        square_feet += sum([2 * side for side in sides]) + min(sides)
    return square_feet

def execute2(puzzle_input):
    presents = puzzle_input.splitlines()
    feet = 0
    for present in presents:
        l, w, h = [int(dimension) for dimension in present.split('x')]
        feet += min([2*l + 2*w, 2*l + 2*h, 2*w + 2*h]) + l*w*h
    return feet