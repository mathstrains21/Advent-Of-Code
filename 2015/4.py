import hashlib


def execute1(puzzle_input):
    number = 0
    while True:
        number += 1
        if (hashlib.md5(
                f"{puzzle_input}{number}".encode()).hexdigest().startswith(
                    "0" * 5)):
            return number


def execute2(puzzle_input):
    number = 0
    while True:
        number += 1
        if (hashlib.md5(
                f"{puzzle_input}{number}".encode()).hexdigest().startswith(
                    "0" * 6)):
            return number
