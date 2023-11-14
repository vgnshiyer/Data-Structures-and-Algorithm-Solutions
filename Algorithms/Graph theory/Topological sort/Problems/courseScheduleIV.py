'''
Kahn's algorithm
- Time: O(V + E)

Does not work with DFS because it gives reverse topological order
'''
def checkIfPrerequisite(n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    adj = defaultdict(list)

    indegree = [0] * n
    prereqs = defaultdict(set)
    for i, j in prerequisites:
        adj[i].append(j)
        indegree[j] += 1
        prereqs[j].add(i)

    q = deque([i for i in range(n) if indegree[i] == 0])
    while q:
        i = q.popleft()
        for j in adj[i]:
            prereqs[j] |= prereqs[i]
            indegree[j] -= 1
            if indegree[j] == 0: q.append(j)

    return [i in prereqs[j] for i, j in queries]