from collections import Counter


def execute1(puzzle_input):
    data = puzzle_input.splitlines()

    cols = [Counter() for _ in range(len(data[0]))]

    # For each row, add the binary number in each column to its counter
    for row in data:
        for i, c in enumerate(row):
            cols[i][c] += 1

    gamma = ""
    epsilon = ""

    for col in cols:
        gamma += col.most_common(1)[0][0]
        epsilon += col.most_common()[-1][0]

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon
