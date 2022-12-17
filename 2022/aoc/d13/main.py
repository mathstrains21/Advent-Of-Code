from typing import IO

def handle_list(packetStr: str)-> list[int, list]:
    packetStr = packetStr[1:-1] # remove square brackets
    packet = []

    item = ""
    nextChar = 0
    for i, char in enumerate(packetStr):
        if i < nextChar:
            continue

        if char == "," and item != "":
            try:
                packet.append(int(item))
            except TypeError:
                packet.append(item)
            item = ""
        elif char == "[":
            layer = 0
            for j, char in enumerate(packetStr[i:], start=i):
                if char == "[":
                    layer += 1
                elif char == "]":
                    layer -= 1
                    if layer == 0:
                        item = handle_list(packetStr[i:j+1])
                        nextChar = j+1
                        break
        else:
            item += char
    
    if item != "":
        try:
            packet.append(int(item))
        except (TypeError, ValueError):
            packet.append(item)
    
    return packet

def parser_1(input_file: IO) -> list[tuple[list[int, list], list[int, list]]]:
    pairString = input_file.read().rstrip().split("\n\n")

    pairs: list[tuple[list[int, list], list[int, list]]] = []

    for pair in pairString:
        packet1String, packet2String = pair.split("\n")
        
        packet1, packet2 = handle_list(packet1String), handle_list(packet2String)

        pairs.append((packet1, packet2))

    return pairs

def parser_2(input_file: IO) -> list[list[int, list]]:
    packetsString = input_file.read().rstrip().split("\n")
    packets = [[[2]], [[6]]]

    for packetString in packetsString:
        if packetString == "":
            continue
        packet = handle_list(packetString)
        packets.append(packet)
    
    return packets

def check_right_order(pair: tuple[list[int, list], list[int, list]]) -> bool:
    packet1, packet2 = pair

    for i, left in enumerate(packet1):
        if i >= len(packet2):
            return False
        right = packet2[i]
        if type(left) == int and type(right) == int:
            if left != right:
                return left < right
            else:
                continue
        
        check_value = tuple()
        if type(left) == list and type(right) == list:
            check_value = (left, right)
        elif type(left) == int and type(right) == list:
            check_value = ([left], right)
        elif type(left) == list and type(right) == int:
            check_value = (left, [right])
        
        checked = check_right_order(check_value)
        if checked is not None:
            return checked
    if len(packet1) < len(packet2):
        return True

def check_all_in_order(packets: list[list[int, list]]) -> bool:
    for i, packet in enumerate(packets):
        if i == 0:
            continue
        if not check_right_order((packets[i-1], packet)):
            return False
    return True

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    pairs: list[tuple[list[int, list], list[int, list]]] = parser_1(input_file)

    indexs: list[int] = []

    for i, pair in enumerate(pairs, start=1):
        correct = check_right_order(pair)
        if correct:
            indexs.append(i)
    
    return sum(indexs)



def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    packets = parser_2(input_file)

    while not check_all_in_order(packets):
        for i, packet in enumerate(packets):
            if i == 0:
                continue
            if not check_right_order((packets[i-1], packet)):
                packets[i-1], packets[i] = packets[i], packets[i-1]
    
    index = 0
    for i, packet in enumerate(packets, start=1):
        if packet == [[2]]:
            index = i
        if packet == [[6]]:
            if index == 0:
                raise ValueError("Packet [[2]] not found")
            return i * index

