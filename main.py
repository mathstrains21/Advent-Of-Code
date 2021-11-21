import typer
import importlib

def main(year: int, day: int, part: int, debug: bool = False):
    module = importlib.import_module(f"{year}.{day}")
    if debug:
        puzzle_input = input('Input: ')
    else:
        with open(f"{year}/{day}.input", "r") as file:
            puzzle_input = file.read()
    print(getattr(module, f"execute{part}")(puzzle_input))

if __name__ == '__main__':
    typer.run(main)