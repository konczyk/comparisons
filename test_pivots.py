import unittest
import pivots


class PivotsTest(unittest.TestCase):

    def test_first_index(self):
        self.assertEqual(pivots.first_index([])(1, 2), 1)

    def test_last_index(self):
        self.assertEqual(pivots.last_index([])(1, 2), 2)

    def test_median_of_three_small(self):
        items = [2, 1]
        self.assertEqual(pivots.median_of_three_index(items)(0, 1), 0)

    def test_median_of_three_odd(self):
        items = [2, 1, 3, 8, 0]
        self.assertEqual(pivots.median_of_three_index(items)(0, 4), 0)

    def test_median_of_three_even(self):
        items = [2, 1, 4, 8, 3, 5]
        self.assertEqual(pivots.median_of_three_index(items)(0, 5), 2)

if __name__ == '__main__':
    unittest.main()
