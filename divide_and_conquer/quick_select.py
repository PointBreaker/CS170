def quick_select(nums, k):
    """
    >>> nums = [3, 5, 9, 2, 7, 0]
    >>> quick_select(nums, 1)
    0
    >>> quick_select(nums, 5)
    7
    >>> quick_select(nums, 3)
    3
    >>> nums = [15, 1, 13, 4, 3, 14, 2, 10, 9, 7, 8, 5, 6, 0, 12, 11]
    >>> quick_select(nums, 2)
    1
    >>> quick_select(nums, 7)
    6
    >>> quick_select(nums, 16)
    15
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
