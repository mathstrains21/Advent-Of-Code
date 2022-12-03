import aoc.d01

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(1, 74, aoc.d01.p_1)

    def test_part_two(self):
        self.run_aoc_part(1, 1795, aoc.d01.p_2)
