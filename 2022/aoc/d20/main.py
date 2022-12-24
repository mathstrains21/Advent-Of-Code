from typing import IO

def parse(input_file: IO) -> list[int]:
    return [int(line) for line in input_file.read().strip().splitlines()]

def is_unique(nums: list[int]) -> bool:
    return len(set(nums)) == len(nums)

def mix(nums: list[int]) -> list[int]:
    order = nums.copy()
    
    for num in order:
        #print(num)
        oldIndex = nums.index(num)
        newIndex = (oldIndex + num) % len(nums) or len(nums) # 0 or num = num

    
        if oldIndex == newIndex:
            continue
        if num > 0:
            if oldIndex < newIndex:
                beg, mid, end = nums[:oldIndex], nums[oldIndex + 1:newIndex + 1], nums[newIndex + 1:]
                nums = [*beg, *mid, num, *end]
            else:
                beg, mid, end = nums[:newIndex + 1], nums[newIndex + 1:oldIndex], nums[oldIndex + 1:]
                nums = [*beg, num, *mid, *end]
        else:
            if oldIndex < newIndex:
                beg, mid, end = nums[:oldIndex], nums[oldIndex + 1:newIndex], nums[newIndex:]
                nums = [*beg, *mid, num, *end]
            else:
                beg, mid, end = nums[:newIndex], nums[newIndex:oldIndex], nums[oldIndex + 1:]
                nums = [*beg, num, *mid, *end]
    
    return nums
        
def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    nums = parse(input_file)

    if not is_unique(nums):
        print(len(nums), len(set(nums)))
        #raise ValueError("Not unique")
    
    nums = mix(nums)
    length = len(nums)

    for i, num in enumerate(nums[nums.index(0) + 1:] + nums * 1000, start=1):
        if i == 1000:
            a = num
            continue
        if i == 2000:
            b = num
            continue
        if i == 3000:
            c = num
            break


    return a + b + c
    



def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    pass
