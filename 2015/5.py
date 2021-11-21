import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def rule1(string):
    count = 0
    for vowel in "aeiou":
        count += string.count(vowel)
    return count >= 3


def rule2(string):
    for letter in ALPHABET:
        if letter * 2 in string:
            return True
    return False


def rule3(string):
    for pair in ["ab", "cd", "pq", "xy"]:
        if pair in string:
            return False
    return True


def execute1(puzzle_input):
    count = 0
    for string in puzzle_input.splitlines():
        if rule1(string) and rule2(string) and rule3(string):
            count += 1
    return count


def rule4(string):
    for a in ALPHABET:
        for b in ALPHABET:
            if string.count(a + b) >= 2:
                return True
    return False


def rule5(string):
    for letter in ALPHABET:
        regexp = re.compile(f"{letter}.{letter}")
        if regexp.search(string):
            return True
    return False


def execute2(puzzle_input):
    count = 0
    for string in puzzle_input.splitlines():
        if rule4(string) and rule5(string):
            count += 1
    return count
