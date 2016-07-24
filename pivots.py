def first_index(items):
    """
    Return first index as a pivot
    """
    return lambda left, right: left


def last_index(items):
    """
    Return last index as a pivot
    """
    return lambda left, right: right


def median_of_three_index(items):
    """
    Return median of three index as a pivot
    """
    def pivot(left, right):
        if right - left < 2:
            return left
        else:
            mid = left + (right - left) // 2
            return sorted([left, right, mid], key=lambda idx: items[idx])[1]

    return pivot
