from functools import cache

@cache
def numSquares(self, n: int) -> int:
    if n == 0: return 0

    ans = 10**4 + 1
    for i in range(1, int(sqrt(n)) + 1):
        ans = min(ans,1 + self.numSquares(n-(i*i)))
    return ans