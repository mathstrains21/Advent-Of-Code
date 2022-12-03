import datetime
import importlib

import typer

today = datetime.date.today()


def main(
    year: int = today.year, day: int = today.day, part: int = 2, debug: bool = False
):
    module = importlib.import_module(f"{year}.{day}")
    if debug:
        puzzle_input = ""
        while True:
            line = input("Input: ")
            if "".join(line.split()) == "":
                break
            puzzle_input += "\n"
            puzzle_input += line
    else:
        with open(f"{year}/{day}.input", "r") as file:
            puzzle_input = file.read()
    print(getattr(module, f"execute{part}")(puzzle_input=puzzle_input))


if __name__ == "__main__":
    typer.run(main)
