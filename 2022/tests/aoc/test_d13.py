import aoc.d13

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(13, 5938, aoc.d13.p_1)

    def test_part_two(self):
        self.run_aoc_part(13, 29025, aoc.d13.p_2)
