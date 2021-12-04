def parse(instruction):
    sections = instruction.split(' ')
    action = None
    coords = []
    if sections[0] == 'toggle':
        action = 'toggle'
        coords = sections[1:]
    elif sections[0] == 'turn':
        if sections[1] == 'on':
            action = 'on'
        elif sections[1] == 'off':
            action = 'off'
        coords = sections[2:]
    return (
        action,
        tuple([int(val) for val in coords[0].split(',')]),
        tuple([int(val) for val in coords[2].split(',')])
    )


def execute1(puzzle_input):
    grid = [[False for _ in range(1000)] for _ in range(1000)]
    for instruction in puzzle_input.splitlines():
        action, beg, end = parse(instruction)
        for x in range(beg[0], end[0]):
            for y in range(beg[1], end[1]):
                if action == 'toggle':
                    grid[x][y] = not grid[x][y]
                elif action == 'on':
                    grid[x][y] = True
                elif action == 'off':
                    grid[x][y] = False
    return len([val for row in grid for val in row if val])
