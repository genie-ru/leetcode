import unittest
from sum import Sum

class TestSum(unittest.TestCase):
    def test_sum_sum(self):
        s = Sum()
        self.assertEqual(s.sum_sum(1, 1), 2)
        self.assertEqual(s.sum_sum(0, 0), 0)
        self.assertEqual(s.sum_sum(0, 0), 0)
        self.assertEqual(s.sum_sum(-1, -1), -2)
        
if __name__ == '__main__':
    unittest.main()