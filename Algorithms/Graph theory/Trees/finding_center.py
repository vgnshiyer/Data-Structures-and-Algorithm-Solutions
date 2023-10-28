def treeCenter(edges, n):
    adj = [[] for _ in range(n)]
    indegree = [0] * n

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
        indegree[x] += 1
        indegree[y] += 1

    leaves = []
    for i in range(n):
        if indegree[i] <= 1:
            leaves.append(i)
            indegree[i] = 0 ## important -> to avoid infinite loops
    count = len(leaves)
    
    while count < n:
        new_leaves = []
        for leaf in leaves:
            for child in adj[leaf]:
                indegree[child] -= 1
                if indegree[child] == 1: new_leaves.append(child) # leaf has to have indegree = 1
        leaves = new_leaves
        count += len(leaves)
    
    return leaves