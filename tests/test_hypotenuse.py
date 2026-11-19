import unittest

from calc.core import calculate
from calc.ops.hypotenuse import hypotenuse


class TestHypotenuse(unittest.TestCase):
    def test_classic_triangle(self):
        self.assertEqual(hypotenuse(3, 4), 5)

    def test_square(self):
        self.assertAlmostEqual(hypotenuse(1, 1), 2 ** 0.5)

    def test_via_calculate(self):
        self.assertEqual(calculate(6, "hyp", 8), 10)
