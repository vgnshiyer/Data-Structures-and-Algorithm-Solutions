def maximumSum(arr: List[int]) -> int:
    '''
    state: dp[i][0] -> max sum till pos i with 0 deletion
            dp[i][1] -> max sum till pos i with 1 deletion 
    transition:
            dp[i][1] = max(arr[i] + dp[i-1][1], dp[i-1][0], arr[i])
            dp[i][0] = max(arr[i], arr[i] + dp[i-1][0])
    base case: dp[0][1] = max(0, arr[0])
                dp[0][0] = arr[0]
    '''
    n = len(arr)

    dp = [[0] * 2 for _ in range(n)]
    dp[0][1] = arr[0]
    dp[0][0] = arr[0]
    best = dp[0][1]

    for i in range(1, n):
        dp[i][1] = max([dp[i-1][0], arr[i], arr[i] + dp[i-1][1]])
        dp[i][0] = max(arr[i], arr[i] + dp[i-1][0])
        best = max(best, dp[i][1])

    return best

def maximumSum_spaceOptimized(self, arr: List[int]) -> int:
    n = len(arr)

    max_withOneDeletion = arr[0]
    max_withNoDeletion = arr[0]
    best = arr[0]

    for i in range(1, n):
        max_withOneDeletion = max([max_withNoDeletion, arr[i], arr[i] + max_withOneDeletion])
        max_withNoDeletion = max(arr[i], arr[i] + max_withNoDeletion)
        best = max(best, max_withOneDeletion)

    return best