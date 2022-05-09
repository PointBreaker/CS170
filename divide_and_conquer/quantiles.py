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

def quantile(nums, k):
    """
    k is power of two
    >>> nums = [15, 1, 13, 4, 3, 14, 2, 10, 9, 7, 8, 5, 6, 0, 12, 11]
    >>> quantile(nums, 1)
    [15]
    >>> quantile(nums, 2)
    [7, 15]
    >>> quantile(nums, 4)
    [3, 7, 11, 15]
    >>> quantile(nums, 8)
    [1, 3, 5, 7, 9, 11, 13, 15]
    >>> quantile(nums, 16)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    >>> nums = [3, 5, 9, 2, 7, 0]
    >>> quantile(nums, 1)
    [9]
    >>> quantile(nums, 2)
    [3, 9]
    >>> quantile(nums, 4)
    [0, 3, 5, 9]
    """
    assert k > 0, "k is 1-index num"
    num_lens = len(nums)
    assert k < num_lens, "k must be less than length"
    if k == 1:
        return [quick_select(nums, num_lens)]
    pivot = quick_select(nums, num_lens // 2)
    left, right = [], []
    for num in nums:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    # print("DEBUG:", left, right)
    return quantile(left, k // 2) + quantile(right, k // 2)
