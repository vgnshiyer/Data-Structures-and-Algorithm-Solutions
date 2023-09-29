def minTaps(n: int, ranges: List[int]) -> int:
    '''
    state: dp[i] -> min number of taps to open for watering from 0 to i
    We initialize this array with a large value like infinity for each position. By doing so, we indicate that no taps have been applied yet, and we can consider these positions as "unreachable" until we find a tap that can water them.
    
    base case: Since we do not have to open any taps to water a part of zero length, thus dp[0]=0.

    transition: for every tap, we get the start and end of the range. For the end of the range we calculate the least amount of taps to open that fills the range 0 to end.
    therefor for j in start, end, dp[j] = min(dp[j], 1 + dp[start])

    For every position j, we try to consider that this part of the garden is not watered thus add 1 to dp[start](which has been watered)
    '''

    INF = 10**9

    dp = [INF] * (n)
    dp[0] = 0

    for i in range(n + 1):
        tap_start = max(0, i - ranges[i])
        tap_end = min(n, i + ranges[i])
        for j in range(tap_start, tap_end + 1):
            dp[j] = min(dp[j], dp[tap_start] + 1)
    return -1 if dp[-1] == INF else dp[-1]