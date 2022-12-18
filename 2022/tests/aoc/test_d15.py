import aoc.d15

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(15, 4907780, aoc.d15.p_1)

    def test_part_two(self):
        self.run_aoc_part(15, False, aoc.d15.p_2)
