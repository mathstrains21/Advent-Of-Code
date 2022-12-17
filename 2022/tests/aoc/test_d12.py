import aoc.d12

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(12, 449, aoc.d12.p_1)

    def test_part_two(self):
        self.run_aoc_part(12, 443, aoc.d12.p_2)
