from typing import IO

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    instructions = input_file.readlines()

    knots = [{"X": 0, "Y": 0} for _ in range(2)]
    allTailPos = {tuple(knots[1].values())}

    for instruction in instructions:
        dir, dist = instruction.split()
        dist = int(dist)

        for _ in range(dist):
            if dir == 'U':
                knots[0]["Y"] += 1
            elif dir == 'D':
                knots[0]["Y"] -= 1
            elif dir == 'R':
                knots[0]["X"] += 1
            elif dir == 'L':
                knots[0]["X"] -= 1
        
            if abs(knots[0]["X"] - knots[1]["X"]) > 1 or abs(knots[0]["Y"] - knots[1]["Y"]) > 1:
                if knots[0]["X"] == knots[1]["X"]:
                    if knots[0]["Y"] > knots[1]["Y"]:
                        knots[1]["Y"] += 1
                    else:
                        knots[1]["Y"] -= 1
                elif knots[0]["Y"] == knots[1]["Y"]:
                    if knots[0]["X"] > knots[1]["X"]:
                        knots[1]["X"] += 1
                    else:
                        knots[1]["X"] -= 1
                else:
                    if knots[0]["X"] > knots[1]["X"] and knots[0]["Y"] > knots[1]["Y"]:
                        knots[1]["X"] += 1
                        knots[1]["Y"] += 1
                    elif knots[0]["X"] > knots[1]["X"] and knots[0]["Y"] < knots[1]["Y"]:
                        knots[1]["X"] += 1
                        knots[1]["Y"] -= 1
                    elif knots[0]["X"] < knots[1]["X"] and knots[0]["Y"] > knots[1]["Y"]:
                        knots[1]["X"] -= 1
                        knots[1]["Y"] += 1
                    elif knots[0]["X"] < knots[1]["X"] and knots[0]["Y"] < knots[1]["Y"]:
                        knots[1]["X"] -= 1
                        knots[1]["Y"] -= 1
                allTailPos.add(tuple(knots[1].values()))
            
    return len(allTailPos)




def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    instructions = input_file.readlines()

    knots = [{"X": 0, "Y": 0} for _ in range(10)]
    allTailPos = {tuple(knots[9].values())}

    for instruction in instructions:
        dir, dist = instruction.split()
        dist = int(dist)

        for _ in range(dist):
            if dir == 'U':
                knots[0]["Y"] += 1
            elif dir == 'D':
                knots[0]["Y"] -= 1
            elif dir == 'R':
                knots[0]["X"] += 1
            elif dir == 'L':
                knots[0]["X"] -= 1
        
            for j in range(1, 10):
                i = j - 1
                if abs(knots[i]["X"] - knots[j]["X"]) > 1 or abs(knots[i]["Y"] - knots[j]["Y"]) > 1:
                    if knots[i]["X"] == knots[j]["X"]:
                        if knots[i]["Y"] > knots[j]["Y"]:
                            knots[j]["Y"] += 1
                        else:
                            knots[j]["Y"] -= 1
                    elif knots[i]["Y"] == knots[j]["Y"]:
                        if knots[i]["X"] > knots[j]["X"]:
                            knots[j]["X"] += 1
                        else:
                            knots[j]["X"] -= 1
                    else:
                        if knots[i]["X"] > knots[j]["X"] and knots[i]["Y"] > knots[j]["Y"]:
                            knots[j]["X"] += 1
                            knots[j]["Y"] += 1
                        elif knots[i]["X"] > knots[j]["X"] and knots[i]["Y"] < knots[j]["Y"]:
                            knots[j]["X"] += 1
                            knots[j]["Y"] -= 1
                        elif knots[i]["X"] < knots[j]["X"] and knots[i]["Y"] > knots[j]["Y"]:
                            knots[j]["X"] -= 1
                            knots[j]["Y"] += 1
                        elif knots[i]["X"] < knots[j]["X"] and knots[i]["Y"] < knots[j]["Y"]:
                            knots[j]["X"] -= 1
                            knots[j]["Y"] -= 1
                    allTailPos.add(tuple(knots[9].values()))
                
    return len(allTailPos)

