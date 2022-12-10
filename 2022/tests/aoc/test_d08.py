import aoc.d08

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(8, 1782, aoc.d08.p_1)

    def test_part_two(self):
        self.run_aoc_part(8, 474606, aoc.d08.p_2)
