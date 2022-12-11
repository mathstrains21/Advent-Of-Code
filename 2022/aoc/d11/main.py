from typing import IO

def get_groups(data: str) -> tuple:
    return (tuple(_.splitlines()) for _ in data.split("\n\n"))

def prod(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

class Monkey:
    barrel = []
    magic = 1

    def __init__(self, d: tuple) -> None:
        self.items = list(map(int, d[1].partition(":")[-1].split(",")))
        self.op = eval(f"lambda old: {d[2].partition('= ')[-1]}")
        self.div = int(d[3].partition("by ")[-1])
        self.throw = tuple(int(_.partition("monkey")[-1]) for _ in d[4:])

        self.count = 0

        self.__class__.magic = self.magic * self.div
        self.barrel.append(self)

    def __call__(self, divisor: int) -> None:
        self.count += len(self.items)
        while self.items:
            w = self.op(self.items.pop()) // divisor
            self.barrel[self.throw[bool(w % self.div)]].items.append(w % self.magic)

    @classmethod
    def business(cls, rounds: int, divisor: int, data: str) -> int:
        for g in get_groups(data):
            cls(g)
        for _ in range(rounds):
            for m in cls.barrel:
                m(divisor)
        try:
            return prod(sorted(m.count for m in cls.barrel)[-2:])
        finally:
            cls.barrel.clear()
            cls.magic = 1

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    return Monkey.business(20, 3, input_file.read())



def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    return Monkey.business(10000, 1, input_file.read())
