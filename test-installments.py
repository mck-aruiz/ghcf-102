import unittest
from your_module import calculate_amortization  # replace 'your_module' with the actual module name

class TestAmortization(unittest.TestCase):
    def test_case_1(self):
        self.assertAlmostEqual(calculate_amortization(100000, 5, 10), 1060.66, places=2)

    def test_case_2(self):
        self.assertAlmostEqual(calculate_amortization(200000, 3.5, 15), 1429.77, places=2)

    def test_case_3(self):
        self.assertAlmostEqual(calculate_amortization(300000, 4.5, 30), 1520.06, places=2)

    def test_case_4(self):
        self.assertAlmostEqual(calculate_amortization(400000, 6, 20), 2869.13, places=2)

    def test_case_5(self):
        self.assertAlmostEqual(calculate_amortization(500000, 5.5, 25), 3086.35, places=2)

if __name__ == '__main__':
    unittest.main()