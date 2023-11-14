def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    adj = defaultdict(list)

    for i, j in prerequisites:
        adj[i].append(j)

    dp = {}
    def dfs(i, t, visited):
        visited.add(i)
        if t == i: return True

        if (i, t) in dp: return dp[(i, t)]
        for j in adj[i]:
            if j in visited: continue
            if dfs(j, t, visited):
                dp[(i, t)] = True
                return True
        dp[(i, t)] = False
        return False

    return [
        dfs(i, j, set()) for i, j in queries
    ]
        