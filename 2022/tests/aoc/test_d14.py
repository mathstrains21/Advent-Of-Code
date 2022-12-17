import aoc.d14

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(14, 799, aoc.d14.p_1)

    def test_part_two(self):
        self.run_aoc_part(14, 29076, aoc.d14.p_2)
