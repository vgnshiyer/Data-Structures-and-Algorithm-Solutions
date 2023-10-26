def treeCenter(adj, n):
    degree = [0] * n
    leaves = []
    for i in range(n): 
        for nxt in adj[i]: degree[nxt] += 1

    for i in range(n):
        if degree[i] == 1: leaves.append(i)

    count = 0
    while count < n:
        count += leaves
        new_leaves = []
        for leaf in leaves:
            for nxt in adj[leaf]:
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    new_leaves.append(nxt)
            degree[leaf] = 0
        leaves = new_leaves
    return leaves # midpoint/s
