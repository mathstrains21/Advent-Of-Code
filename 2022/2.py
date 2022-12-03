def execute1(puzzle_input):
    data = puzzle_input.splitlines()
    score = 0

    for line in data:
        if 'A Y' in line or 'B Z' in line or 'C X' in line:
            score += 6
        elif 'A X' in line or 'B Y' in line or 'C Z' in line:
            score += 3

        if 'X' in line:
            score += 1
        elif 'Y' in line:
            score += 2
        else:
            score += 3
    return score

def execute2(puzzle_input):
    data = puzzle_input.splitlines()
    score = 0

    for line in data:
        if 'Z' in line:
            score += 6
            if 'A' in line:
                score += 2
            elif 'B' in line:
                score += 3
            else:
                score += 1
        elif 'Y' in line:
            score += 3
            if 'A' in line:
                score += 1
            elif 'B' in line:
                score += 2
            else:
                score += 3
        else:
            if 'A' in line:
                score += 3
            elif 'B' in line:
                score += 1
            else:
                score += 2

    return score