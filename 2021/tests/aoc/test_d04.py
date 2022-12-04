import aoc.d04

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(4, 50008, aoc.d04.p_1)

    def test_part_two(self):
        self.run_aoc_part(4, 17408, aoc.d04.p_2)
