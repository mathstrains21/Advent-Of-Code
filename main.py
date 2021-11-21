import typer
import importlib

def main(year: int, day: int, part: int):
    module = importlib.import_module(f"{year}.{day}")
    with open(f"{year}/{day}.input", "r") as file:
        input = file.read()
    print(getattr(module, f"execute{part}")(input))

if __name__ == '__main__':
    typer.run(main)