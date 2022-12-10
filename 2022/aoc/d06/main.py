from typing import IO
from queue import Queue

class Buffer(Queue):
    def safe_put(self, value):
        if self.full():
            self.get()
        self.put(value)
    
    def check_unique(self):
        return len(set(self.queue)) == len(self.queue)

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    buffer = Buffer(4)
    chars = input_file.read()
    for char in chars[:3]:
        buffer.put(char)
    for pos, char in enumerate(chars[3:], start=4):
        buffer.safe_put(char)
        if buffer.check_unique():
            return pos


def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    buffer = Buffer(14)
    chars = input_file.read()
    for char in chars[:13]:
        buffer.put(char)
    for pos, char in enumerate(chars[13:], start=14):
        buffer.safe_put(char)
        if buffer.check_unique():
            return pos

