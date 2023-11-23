def mostProfitablePath(edges: List[List[int]], bob: int, amount: List[int]) -> int:
    n = len(edges)
    # min distance of a node from alice (0)
    alice_dis = [0] * (n + 1)
    # path taken to that node
    parent = [0] * (n + 1)

    adj = defaultdict(list)
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)

    def dfs(i, p, d):
        alice_dis[i] = d
        parent[i] = p
        for j in adj[i]:
            # avoid going back
            if j != p: dfs(j, i, d + 1)

    def dfs2(i, p = -1):
        # max from this node
        max_here = -inf
        for j in adj[i]:
            if j != p:
                max_here = max(max_here, dfs2(j, i))
        # if leaf, return cur node cost
        return (max_here if max_here > -inf else 0) + amount[i]

    # find distances and paths
    dfs(0, -1, 0)

    bob_dis = 0
    while bob != 0:
        # bob reaches first to this node --> alice gets nothing
        if alice_dis[bob] > bob_dis:
            amount[bob] = 0
        # both arrive at the same time --> split the amount
        elif alice_dis[bob] == bob_dis:
            amount[bob] = amount[bob] // 2
        bob = parent[bob]
        bob_dis += 1

    # return the best path for alice
    return dfs2(0)