class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.m = 0
        while self.n >= (1 << self.m): self.m += 1
        self.m += 1

        self.dp = [[-1] * self.m for _ in range(self.n)]
        for i in range(self.n): self.dp[i][0] = parent[i]

        ## 2^j ancestors for all nodes -- O(n logn)
        for j in range(1, self.m):
            for i in range(self.n):
                if self.dp[i][j - 1] == -1: continue
                self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        ## jumping powers of 2 -- O(logn)
        while k and node != -1:
            if k & 1: node = self.dp[node][i]
            k >>= 1
            i += 1
        return node