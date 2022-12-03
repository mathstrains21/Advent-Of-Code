from typing import IO
from collections import Counter

def parse_bit_pos(arr, pos):
    
    return Counter(row[pos] for row in arr)

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    data = input_file.readlines()

    cols: list = [Counter() for _ in range(len(data[0]))]

    # For each row, add the binary number in each column to its counter
    for row in data:
        for i, c in enumerate(row):
            cols[i][c] += 1

    gamma = ""
    epsilon = ""

    for col in cols:
        gamma += col.most_common(1)[0][0]
        epsilon += col.most_common()[-1][0]

    gamma1 = int(gamma, 2)
    epsilon1 = int(epsilon, 2)

    return gamma1 * epsilon1



def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    data = [[int(n) for n in line.strip()] for line in input_file.readlines()]
    L1 = L2 = data
    for i in range(len(data[0])):
        c1, c2 = parse_bit_pos(L1, i), parse_bit_pos(L2, i)
        
        if len(L1) > 1:
            if len(set(c1.values())) == 1:
                L1 = [row for row in L1 if row[i] == 1]
            else:
                L1 = [row for row in L1 if row[i] == max(c1.items(), key=lambda x: x[1])[0]]
        if len(L2) > 1:
            if len(set(c2.values())) == 1:
                L2 = [row for row in L2 if row[i] == 0]
            else:
                L2 = [row for row in L2 if row[i] == min(c2.items(), key=lambda x: x[1])[0]]
            
    o2, co2 = int(''.join([str(n) for n in L1[0]]), 2), int(''.join([str(n) for n in L2[0]]), 2)
    return o2 * co2
