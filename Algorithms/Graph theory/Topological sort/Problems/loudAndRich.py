
def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)

    richerThan = defaultdict(list)
    for a, b in richer:
        richerThan[a].append(b)

    temp = [(None, inf) for x in range(n)]

    def dfs(i, j):
        if j[1] < temp[i][1]:
            temp[i] = j
            for k in richerThan[i]:
                dfs(k, temp[i])

    answer = []
    for i in range(n):
        dfs(i, (i, quiet[i]))
        
    for i in range(n):
        answer.append(temp[i][0])

    return answer
    

def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    indegree = [0] * n
    adj = defaultdict(list)
    for a, b in richer:
        indegree[b] += 1
        adj[a].append(b)

    q = deque()
    for i in range(n):
        if indegree[i] == 0: q.append(i)

    answer = [i for i in range(n)]
    while q:
        i = q.popleft()

        for j in adj[i]:
            if quiet[answer[i]] < quiet[answer[j]]:
                answer[j] = answer[i]
            
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
    return answer 