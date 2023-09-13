'''
This problem is similar to min taps
'''

def jumpGame(nums: list[int]) -> int:
    n = len(nums)
    dp = [10 ** 9] * n
    dp[0] = 0

    for i in range(n):
        start = i
        end = min(i + nums[i], n-1)
        for j in range(start, end + 1):
            dp[j] = min(dp[j], dp[start] + 1)

    return -1 if dp[-1] == 10 ** 9 else dp[-1]