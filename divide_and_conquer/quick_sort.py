def quick_sort(nums):
    """"
    You know what this does
    >>> nums = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
    >>> quick_sort(nums)
    [1, 2, 4, 5, 5, 8, 11, 13, 20, 21, 36]
    >>> nums = []
    >>> quick_sort(nums)
    []
    >>> nums = [1, 2, 3, 4, 5]
    >>> quick_sort(nums)
    [1, 2, 3, 4, 5]
    >>> nums = [-1, 1, 0]
    >>> quick_sort(nums)
    [-1, 0, 1]
    >>> nums = [5, 3, 1, 0, -2]
    >>> quick_sort(nums)
    [-2, 0, 1, 3, 5]
    """
    nums_len = len(nums)
    if nums_len <= 0:
        return nums
    pivot = nums[0]
    small, large = [], []
    for num in nums[1:]:
        if num <= pivot:
            small.append(num)
        else:
            large.append(num)
    return quick_sort(small) + [pivot] + quick_sort(large)