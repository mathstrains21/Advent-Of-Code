from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    data = input_file.readlines()
    score = 0

    for line in data:
        if "A Y" in line or "B Z" in line or "C X" in line:
            score += 6
        elif "A X" in line or "B Y" in line or "C Z" in line:
            score += 3

        if "X" in line:
            score += 1
        elif "Y" in line:
            score += 2
        else:
            score += 3
    return score


def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    data = input_file.readlines()
    score = 0

    for line in data:
        if "Z" in line:
            score += 6
            if "A" in line:
                score += 2
            elif "B" in line:
                score += 3
            else:
                score += 1
        elif "Y" in line:
            score += 3
            if "A" in line:
                score += 1
            elif "B" in line:
                score += 2
            else:
                score += 3
        else:
            if "A" in line:
                score += 3
            elif "B" in line:
                score += 1
            else:
                score += 2

    return score

