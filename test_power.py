import unittest
from power import power

class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertTrue(power(2,3), 8)

if __name__ == "__main__":
    unittest.main()
