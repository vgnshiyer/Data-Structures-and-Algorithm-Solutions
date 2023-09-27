def minSteps(n: int) -> int:
    if n == 1: return 0

    @cache
    def getMinOperations(numChars, clipBoard):
        if numChars == n: return 0
        if numChars > n: return float('inf')

        ## paste
        ans = 1 + getMinOperations(numChars + clipBoard, clipBoard)

        ## copy + paste
        ans = min(ans, 2 + getMinOperations(numChars * 2, numChars))
        return ans

    return getMinOperations(1, 1) + 1