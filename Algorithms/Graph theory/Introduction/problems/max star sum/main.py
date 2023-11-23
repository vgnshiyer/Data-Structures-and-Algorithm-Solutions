def maxStarSum(vals: List[int], edges: List[List[int]], k: int) -> int:
    adj = defaultdict(list)
    for i, j in edges:
        # sort child nodes by max vals
        if vals[j] > 0: heappush(adj[i], (-vals[j], j))
        if vals[i] > 0: heappush(adj[j], (-vals[i], i))

    max_sum = -inf
    # consider each node as the center of the star
    for i, v in enumerate(vals):
        # find max k childs
        sum_ = v
        c = 0
        while adj[i] and c < k:
            sum_ += -(heappop(adj[i]))[0]
            c += 1
        # record max
        max_sum = max(max_sum, sum_)
    return max_sum