from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    data = input_file.read().splitlines()

    increased = 0
    previous = int(data[0])
    for number in data[1:]:
        if int(number) > previous:
            increased += 1
        previous = int(number)
    return increased


def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    nums = [int(n) for n in input_file.read().splitlines()]
    return sum(
        a + b + c < b + c + d for a, b, c, d in zip(nums, nums[1:], nums[2:], nums[3:])
    )
