#!/usr/bin/env python3

import unittest
import pivots
from comparisons import Comparisons


class ComparisonsTest(unittest.TestCase):

    def test_empty(self):
        items = []
        comp = Comparisons(items)

        self.assertEqual(comp.count(), 0)

    def test_one(self):
        items = [1]
        comp = Comparisons(items)

        self.assertEqual(comp.count(), 0)

    def test_first_index_pivot(self):
        items = [3, 4, 5, 1, 8]
        comp = Comparisons(items, pivots.first_index)

        self.assertEqual(comp.count(), 6)

    def test_last_index_pivot(self):
        items = [1, 8, 3, 2, 5, 4]
        comp = Comparisons(items, pivots.last_index)

        self.assertEqual(comp.count(), 8)

    def test_median_of_three_pivot(self):
        items = [0, 3, 7, 2, 9, 8]
        comp = Comparisons(items, pivots.median_of_three_index)

        self.assertEqual(comp.count(), 8)

if __name__ == '__main__':
    unittest.main()
