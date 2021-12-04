def execute1(puzzle_input):
    increased = 0
    previous = int(puzzle_input.splitlines()[0])
    for number in puzzle_input.splitlines()[1:]:
        if int(number) > previous:
            increased += 1
        previous = int(number)
    return increased


def execute2(puzzle_input):
    nums = [int(n) for n in puzzle_input.splitlines()]
    return sum(
        a + b + c < b + c + d
        for a, b, c, d in zip(nums, nums[1:], nums[2:], nums[3:])
    )
