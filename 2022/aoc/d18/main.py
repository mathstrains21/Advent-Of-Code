from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    lines = input_file.read().strip().split('\n')
    coords: list[tuple[int, int, int]] = []
    for line in lines:
        x, y, z = line.split(',')
        coords.append((int(x), int(y), int(z)))
    
    exposed = 0
    for x, y, z in coords:
        if (x + 1, y, z) not in coords:
            exposed += 1
        if (x - 1, y, z) not in coords:
            exposed += 1
        if (x, y + 1, z) not in coords:
            exposed += 1
        if (x, y - 1, z) not in coords:
            exposed += 1
        if (x, y, z + 1) not in coords:
            exposed += 1
        if (x, y, z - 1) not in coords:
            exposed += 1
    
    return exposed


def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    pass
