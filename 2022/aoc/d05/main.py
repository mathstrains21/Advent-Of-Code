from typing import IO
from queue import LifoQueue as Stack

def process_input(input_file: IO):
    stackBigString, instructionsBigString = input_file.read().split("\n\n")
    *stacksStrings, stackNames = stackBigString.split("\n")
    
    stackNums = [int(s) for s in stackNames.split()]
    stacks = {stackNum: Stack() for stackNum in stackNums}

    stacksLists = []
    for stackString in stacksStrings:
        stackList = []
        i = 0
        while i < len(stackString):
            crate = stackString[i:i+4]
            stackList.append(crate.strip().strip("[").strip("]"))
            i += 4
        stacksLists.append(stackList)

    for stackList in stacksLists[::-1]:
        for i, crate in enumerate(stackList):
            if crate != "":
                stacks[i + 1].put(crate)

    instructionsLists = instructionsBigString.splitlines()
    instructions = []
    for instructionList in instructionsLists:
        instruction = instructionList.split()[1::2]
        instructions.append([int(num) for num in instruction])

    return stacks, instructions


def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    stacks, instructions = process_input(input_file)

    for instruction in instructions:
        num, source, dest = instruction
        for _ in range(num):
            x = stacks[source].get()
            stacks[dest].put(x)
    top_crates = "".join([stack.get() for stack in stacks.values()])
    return top_crates
      



def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    stacks, instructions = process_input(input_file)

    for instruction in instructions:
        num, source, dest = instruction
        holdingBay = Stack()
        for _ in range(num):
            x = stacks[source].get()
            holdingBay.put(x)
        while not holdingBay.empty():
            x = holdingBay.get()
            stacks[dest].put(x)
    top_crates = "".join([stack.get() for stack in stacks.values()])
    return top_crates

