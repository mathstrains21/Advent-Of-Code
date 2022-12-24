import aoc.d20

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(20, False, aoc.d20.p_1)

    def test_part_two(self):
        self.run_aoc_part(20, False, aoc.d20.p_2)
