def mctFromLeafValues(self, arr: List[int]) -> int:
    '''
    returning 2 things
    [minSum for subtree, max leaf val]
    '''
    n = len(arr)
    dp = [[(0, 0)] * n for _ in range(n)]
    for i in range(n): dp[i][i] = (0, arr[i])

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            ans = float('inf')
            leaf_val = -1
            for k in range(i, j):
                left_sum, left_leaf = dp[i][k]
                right_sum, right_leaf = dp[k+1][j]

                cur_node_val = left_leaf * right_leaf
                max_leaf = max(left_leaf, right_leaf)

                if left_sum + right_sum + cur_node_val < ans:
                    ans = left_sum + right_sum + cur_node_val
                    leaf_val = max_leaf

            dp[i][j] = (ans, leaf_val)

    return dp[0][n-1][0]