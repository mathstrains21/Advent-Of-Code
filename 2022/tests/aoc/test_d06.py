import aoc.d06

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(6, 1779, aoc.d06.p_1)

    def test_part_two(self):
        self.run_aoc_part(6, 2635, aoc.d06.p_2)
