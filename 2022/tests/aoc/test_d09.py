import aoc.d09

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(9, 5883, aoc.d09.p_1)

    def test_part_two(self):
        self.run_aoc_part(9, 2367, aoc.d09.p_2)
