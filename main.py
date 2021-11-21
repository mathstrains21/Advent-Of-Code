import typer
import importlib

def main(year: int, day: int, part: int):
    module = importlib.import_module(f"{year}.{day}")
    getattr(module, f"execute{part}")()

if __name__ == '__main__':
    typer.run(main)