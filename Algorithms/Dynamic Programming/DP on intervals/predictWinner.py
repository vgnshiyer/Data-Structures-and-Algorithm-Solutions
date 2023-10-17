
def predictTheWinner_recursive(nums: List[int]) -> bool:
    @cache
    def minimax(i, j, maxPlayer):
        if i == j: return nums[i] if maxPlayer else -nums[i]
        
        if maxPlayer:
            score = max(nums[i] + minimax(i + 1, j, False),
                        nums[j] + minimax(i, j - 1, False))
        else:
            score = min(-nums[i] + minimax(i + 1, j, True),
                        -nums[j] + minimax(i, j - 1, True))
        return score
            
    score = minimax(0, len(nums) - 1, True) ## player 1 starts first

    return score >= 0


def predictTheWinner_iterative(nums: List[int]) -> bool:
    n = len(nums)
    dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j: 
                dp[i][j] = [-nums[i], nums[i]]
            else:
                dp[i][j][1] = max(nums[i] + dp[i + 1][j][0], nums[j] + dp[i][j - 1][0])
                dp[i][j][0] = min(-nums[i] + dp[i + 1][j][1], -nums[j] + dp[i][j - 1][1])
        
    return dp[0][n-1][1] >= 0

def predictTheWinner_spaceOptimized(nums: List[int]) -> bool:
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j: 
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
    return dp[0][n-1] >= 0