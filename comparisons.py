#!/usr/bin/env python3


class Comparisons:
    """
    Quick sort implementation with comparisons counting for inputs with no
    repeated values
    """

    def __init__(self, items, pivot=lambda x: lambda left, right: left):
        """
        Copy the list of items and set comparisons to 0
        """

        self._items = list(items)
        self._comparisons = 0
        self._pivot = pivot

    def count(self):
        """
        Count the number of comparisons used to sort the input by Quick Sort
        """
        self._sort(0, len(self._items) - 1)

        return self._comparisons

    def _sort(self, left, right):
        """
        Sort the subitems by recursive split using the pivot function
        """
        if right <= left:
            return
        else:
            pivot = self._pivot(self._items)(left, right)
            # always make the pivot the first element
            if pivot > 0:
                self._swap(left, pivot)

            split = self._partition(left, right)
            self._comparisons += right - left

            # recursive calls
            self._sort(left, split - 1)
            self._sort(split + 1, right)

    def _partition(self, left, right):
        """
        Partition the subitems so that
        everything to the left of the pivot is less than the pivot and
        everything to the right of the pivot is greater than the pivot
        """
        i, j = left, left + 1
        while j <= right:
            if self._items[j] < self._items[left]:
                i += 1
                if i < j:
                    self._swap(j, i)
            j += 1

        # put pivot element in place
        if i > left:
            self._swap(left, i)

        return i

    def _swap(self, a, b):
        self._items[a], self._items[b] = self._items[b], self._items[a]

