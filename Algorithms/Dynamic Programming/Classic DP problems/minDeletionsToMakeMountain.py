def minimumMountainRemovals(nums: List[int]) -> int:
    '''
    Try inverting the problem statement.
    Instead of finding the minimum number of removals, find the maximum number of elements that can be kept such that it maintains the mountain property.

    Can LIS help? We can find the LIS from left to right and right to left.
    At every index we do (LIS_left[i] + LIS_right[i] - 1). This gives us the maximum length of mountain array with i as the peak.
    Keep in mind that, the array can be a slope. Therefore we make sure that LIS_left[i] > 1 and LIS_right[i] > 1.
    '''

    n = len(nums)
    left, right = [1] * n, [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]: left[i] = max(left[i], left[j] + 1)
    
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if nums[j] < nums[i]: right[i] = max(right[i], right[j] + 1)

    best = 0
    for i in range(n):
        if left[i] > 1 and right[i] > 1:
            best = max(best, left[i] + right[i] - 1)
    return n - best