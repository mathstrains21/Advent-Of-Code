import aoc.d10

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(10, 15260, aoc.d10.p_1)

    def test_part_two(self):
        self.run_aoc_part(10, 15260, aoc.d10.p_2)
