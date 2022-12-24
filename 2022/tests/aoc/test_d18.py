import aoc.d18

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(18, 4456, aoc.d18.p_1)

    def test_part_two(self):
        self.run_aoc_part(18, False, aoc.d18.p_2)
