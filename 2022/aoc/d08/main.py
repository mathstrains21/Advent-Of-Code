from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    data = input_file.read()
    rows = [[int(num) for num in row] for row in data.splitlines()]
    columns = [list(column) for column in zip(*rows)]

    visibles = 0
    for i, row in enumerate(rows):
        for j, tree in enumerate(row):
            visible = False

            if i == 0 or j == 0 or i == len(rows) - 1 or j == len(row) - 1: # Outside
                visible = True
            elif max(row[:j]) < tree or max(row[j + 1:]) < tree: # Left or right
                visible = True
            elif max(columns[j][:i]) < tree or max(columns[j][i + 1:]) < tree: # Top or bottom
                visible = True

            if visible:
                visibles += 1

    return visibles

def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    data = input_file.read()
    rows = [[int(num) for num in row] for row in data.splitlines()]
    columns = [list(column) for column in zip(*rows)]

    bestScenicScore = 0
    for i, row in enumerate(rows):
        for j, tree in enumerate(row):
            if i == 0 or j == 0 or i == len(rows) - 1 or j == len(row) - 1: # Outside
                scenicScore = 0 # 0 * anything = 0
            else:
                left = j
                for k, t in enumerate(row[:j][::-1], start=1):
                    if t >= tree:
                        left = k
                        break
                
                right = len(row) - j - 1
                for k, t in enumerate(row[j + 1:], start=1):
                    if t >= tree:
                        right = k
                        break
                
                top = i
                for k, t in enumerate(columns[j][:i][::-1], start=1):
                    if t >= tree:
                        top = k
                        break
                
                bottom = len(columns[j]) - i - 1
                for k, t in enumerate(columns[j][i + 1:], start=1):
                    if t >= tree:
                        bottom = k
                        break
                
                scenicScore = left * right * top * bottom
                if scenicScore > bestScenicScore:
                    bestScenicScore = scenicScore

    return bestScenicScore

