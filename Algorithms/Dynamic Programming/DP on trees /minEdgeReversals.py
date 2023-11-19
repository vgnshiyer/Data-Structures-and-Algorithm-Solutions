def minEdgeReversals(n: int, edges: List[List[int]]) -> List[int]:
    adj = defaultdict(list)
    for i, j in edges:
        adj[i].append((j, 0))
        # add counter edge
        adj[j].append((i, 1))

    # dp[i] => min edge reversals to reach all nodes in the subtree of i
    dp = [-1] * n

    def dfs(i, p = -1):
        if dp[i] == -1:
            ans = 0
            for j, c in adj[i]:
                if j != p:
                    # add cost to reach node and further costs
                    ans += (c + dfs(j, i))
            dp[i] = ans

        return dp[i]

    # compute min reversals for subtrees
    dfs(0)

    ans = [0] * n
    # min reversals already computed for root node
    ans[0] = dp[0]

    def dfs2(i, p = -1, c = 0):
        if p != -1:
            # cost for node i will be included in its parent
            # we only need to consider the edge between current node and its parent (1 if x --> y else -1 (an extra reversal will be counted by parent which we dont need for current node))
            ans[i] = ans[p] + [1, -1][c]

        for j, c in adj[i]:
            if j != p:
                dfs2(j, i, c)

    dfs2(0)

    return ans