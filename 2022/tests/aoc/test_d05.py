import aoc.d05

from tests.aoc.test_base import BaseTestCase


class TestAll(BaseTestCase):
    def test_part_one(self):
        self.run_aoc_part(5, "ZBDRNPMVH", aoc.d05.p_1)

    def test_part_two(self):
        self.run_aoc_part(5, "WDLPFNNNB", aoc.d05.p_2)
