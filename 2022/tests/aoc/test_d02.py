import aoc.d02
from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(2, 15632, aoc.d02.p_1)

    def test_part_two(self):
        self.run_aoc_part(2, 14416, aoc.d02.p_2)
