def first_index(left, *args):
    """
    Return first index as a pivot
    """
    return left


def last_index(left, right, *args):
    """
    Return last index as a pivot
    """
    return right


def median_of_three_index(left, right, items):
    """
    Return median of three index as a pivot
    """
    if right - left < 2:
        return left
    else:
        mid = left + (right - left) // 2
        return sorted([left, right, mid], key=lambda idx: items[idx])[1]
