def merge_sort(nums):
    """
    You know what this can do
    >>> nums = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
    >>> merge_sort(nums)
    [1, 2, 4, 5, 5, 8, 11, 13, 20, 21, 36]
    >>> nums = []
    >>> merge_sort(nums)
    []
    >>> nums = [1, 2, 3, 4, 5]
    >>> merge_sort(nums)
    [1, 2, 3, 4, 5]
    >>> nums = [-1, 1, 0]
    >>> merge_sort(nums)
    [-1, 0, 1]
    >>> nums = [5, 3, 1, 0, -2]
    >>> merge_sort(nums)
    [-2, 0, 1, 3, 5]
    """
    nums_len = len(nums)
    if nums_len > 1:
        return merge(merge_sort(nums[0: nums_len // 2]), merge_sort(nums[nums_len // 2:]))
    return nums

def merge(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    if l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])