import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        s = Solution()
        self.assertAlmostEqual(s.findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertAlmostEqual(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertAlmostEqual(s.findMedianSortedArrays([0, 0], [0, 0]), 0.0)
        self.assertAlmostEqual(s.findMedianSortedArrays([], [1]), 1.0)
        self.assertAlmostEqual(s.findMedianSortedArrays([2], []), 2.0)

if __name__ == '__main__':
    unittest.main()
