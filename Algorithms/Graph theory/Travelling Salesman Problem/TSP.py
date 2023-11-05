def TSP_recursive(prev, mask):
    if (prev, mask) in dp: return dp[(prev, mask)]
    if mask == (1 << n) - 1:
        return 0 ## all nodes visited
        
    cost = inf
    for i in range(n):
        if mask & (1 << i): continue
        cost = min(cost, dist[prev][i] + TSP(i, mask | (1 << i)))
    dp[(prev, mask)] = cost # memoize 
    return cost
     
def TSP_iterative():
    dp = [[inf] * (1 << n) for _ in range(n)]
    
    for i in range(n): dp[i][(1 << i)] = 0
    
    for mask in range(1, 1 << n):
        for i in range(n): # already included
            if mask & (1 << n):
                for j in range(n): # include a new node
                    if i != j and mask & (1 << j): continue
                    dp[j][mask | (1 << j)] = min(
                                                dp[j][mask | (1 << j)], 
                                                dp[i][mask] + dist[i][j]
                                            )

    return min([
            x[(1 << n) - 1] for x in dp[i]
        ], default = inf)
         