def quick_select(nums, k):
    """
    return the k-th smallest number in nums
    >>> v = [1, -1, -1, 1]
    >>> matrix_vector(v, 4)
    [0, 0, 0, 4]
    >>> v = [1, 2, 3, 4]
    >>> matrix_vector(v, 4)
    [10, -2, -4, 0]
    """
    assert k > 0, "k is 1-index num"
    pivot = nums[0]
    small, v, large = [], [], []
    for num in nums:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            large.append(num)
        else:
            v.append(num)
    if k <= len(small):
        return quick_select(small, k)
    elif k > len(small) + len(v):
        return quick_select(large, k - len(small) - len(v))
    else:
        return pivot
