def quick_select(nums, k):
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
