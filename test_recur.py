import unittest
from recur import sum_number

class TestRecur(unittest.TestCase):
    def sum_number(self):
        self.assertEqual(sum_number([2,5,3,[2,7],8]), 27 )

if __name__ == "__main__":
    unittest.main()