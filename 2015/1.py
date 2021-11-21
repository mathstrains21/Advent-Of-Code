def execute1(input):
    floor = 0
    for bracket in input:
        if bracket == '(':
            floor += 1
        elif bracket == ')':
            floor -= 1
    return floor

def execute2(input):
    floor = 0
    for position, bracket in enumerate(input):
        if floor == -1:
            return position
        if bracket == '(':
            floor += 1
        elif bracket == ')':
            floor -= 1