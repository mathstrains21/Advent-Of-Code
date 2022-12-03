priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def chunked(my_list, step):
    start = 0
    end = len(my_list)
    list = []
    for i in range(start, end, step):
        x = i
        list.append(my_list[x : x + step])
    return list


def execute1(puzzle_input):
    data = puzzle_input.splitlines()
    total = 0
    for line in data:
        line_len_half = len(line) // 2
        a, b = line[:line_len_half], line[line_len_half:]
        a, b = set(a), set(b)
        letter = (a & b).pop()
        total += priorities.index(letter)
    return total


def execute2(puzzle_input):
    data = chunked(puzzle_input.splitlines(), 3)
    total = 0
    for chunk in data:
        letter = (set(chunk[0]) & set(chunk[1]) & set(chunk[2])).pop()
        total += priorities.index(letter)
    return total
