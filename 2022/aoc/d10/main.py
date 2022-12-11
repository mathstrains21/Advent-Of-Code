from typing import IO

def get_cycles(input_file: IO):
    instructions = input_file.read().splitlines()

    cycles = {}
    cycle_num = 1
    x = 1
    for instruction in instructions:
        if instruction == "noop":
            cycles[cycle_num] = x
            cycle_num += 1
        else:
            cycles[cycle_num] = x
            cycle_num += 1
            cycles[cycle_num] = x
            cycle_num += 1
            x += int(instruction.split()[1])
    
    return cycles

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    cycles = get_cycles(input_file)
    return cycles[20] * 20 + cycles[60] * 60 + cycles[100] * 100 + cycles[140] * 140 + cycles[180] * 180 + cycles[220] * 220


def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    data = input_file.read()

    data_list = data.split("\n")

    x = 1
    cycles = 0 
    total = 0 
    beam_pos = 0 
    processing = False
    line = 0
    text = ""
    for i in range(240):
        if beam_pos > 39:
            beam_pos = 0 
            text += "\n"
        if beam_pos <= x+1 and beam_pos >= x-1:
            text += "#"
        else:
            text += "."
        if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
            total += (cycles*x)
        if processing == False:
            if data_list[line] == "noop":
                cycles += 1 
                beam_pos += 1
                line += 1
            elif data_list[line][:4] == "addx":
                processing = True
                cycles += 1 
                beam_pos += 1
        elif processing == True:
            cycles += 1
            beam_pos += 1
            x += int(data_list[line][4:])
            line += 1
            processing = False
        

    print(text)
    return total
