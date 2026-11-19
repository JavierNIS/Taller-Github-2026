import unittest

from calc.core import OPERATIONS, calculate, format_result, parse_number


class TestCalculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtract(self):
        self.assertEqual(calculate(10, "-", 4), 6)

    def test_divide(self):
        self.assertEqual(calculate(8, "/", 2), 4)
    
    def test_max(self):
        self.assertEqual(calculate(8, "max", 2), 8)
        self.assertEqual(calculate(2, "max", 8), 8)

    def test_min(self):
        self.assertEqual(calculate(8, "min", 2), 2)
        self.assertEqual(calculate(2, "min", 8), 2)

    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            calculate(1, "?", 2)

    def test_every_operation_is_callable(self):
        for symbol, operation in OPERATIONS.items():
            with self.subTest(symbol=symbol):
                self.assertTrue(callable(operation))


class TestParseNumber(unittest.TestCase):
    def test_dot_and_comma(self):
        self.assertEqual(parse_number("3.5"), 3.5)
        self.assertEqual(parse_number(" 3,5 "), 3.5)

    def test_rejects_text(self):
        with self.assertRaises(ValueError):
            parse_number("hola")

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            parse_number("   ")


class TestFormatResult(unittest.TestCase):
    def test_integer_float(self):
        self.assertEqual(format_result(4.0), "4")

    def test_float_noise(self):
        self.assertEqual(format_result(0.1 + 0.2), "0.3")
