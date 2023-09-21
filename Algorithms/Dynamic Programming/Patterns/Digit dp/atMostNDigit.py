'''
The 1 added in answer and line number 11 represents that we are counting the number we got so far.
Notice that in this problem we are asked to form all possible numbers regardless of the number of digits in the number.
Therefore, we do not have to wait till i == n for adding the ans. The current number can be added.

Notice that line number 11 is an optimization. As the prefix is not same, we have the liberty to choose any of [0-9].
'''
def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
    digits = list(map(int, digits))
    n = list(map(int, str(n)))

    @cache
    def dfs(i, isPrefix, isBigger):
        if i >= len(n): return not isBigger
        if not isPrefix: return 1 + len(digits) * dfs(i + 1, False, isBigger)

        ans = 1
        for d in digits:
            ans += dfs(i + 1, isPrefix and d == n[i], isBigger or d > n[i])
        return ans

    return dfs(0, True, False) - 1