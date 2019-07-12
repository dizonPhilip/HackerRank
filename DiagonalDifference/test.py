import unittest
from diagonal_difference import diagonalDifference

class DiagonalDifferenceTest(unittest.TestCase):
    def test_1(self):
        arr= (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
        )
        result = diagonalDifference(arr)
        self.assertEqual(0, result)
    
    def test_2(self):
        arr= (
            (1,   2,  3,  4),
            (5,   6,  7,  8),
            (9,  10, 11, 12),
            (13, 14, 15, 16),
        )
        result = diagonalDifference(arr)
        self.assertEqual(0, result)

    def test_32(self):
        arr= (
            (1, 2),
            (5, 3),
        )
        result = diagonalDifference(arr)
        self.assertEqual(3, result)

if __name__ == "__main__":
    unittest.main()


