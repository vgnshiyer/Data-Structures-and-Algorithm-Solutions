'''
Approach 1: 
- We use topological sort to traverse back from a course to go all the way back and complete its prerequisites
- Among the prerequisites, we choose the one that takes the most time to complete
- We add the max time take for completing its prerequisites and add it to the time taken to complete the current course
- We also store the maxTime required to complete a couse as multiple courses can have the same prerequisite
- At last we return the maxTime required to complete all the courses
'''
def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    adj = defaultdict(list)
    for r in relations:
        pre, course = r
        adj[course].append(pre)

    dp = {}

    def getMinimumTime(course):
        if course in dp: return dp[course]

        maxTimeToCompletePrereq = 0
        for pre in adj[course]:
            maxTimeToCompletePrereq = max(maxTimeToCompletePrereq, getMinimumTime(pre))

        dp[course] = maxTimeToCompletePrereq + time[course - 1]
        return dp[course]

    maxTime = -1
    for course in range(1, n + 1):
        maxTime = max(maxTime, getMinimumTime(course))
    return maxTime

'''
Approach 2:
- We use a push-dp type approach
- We store the indegree count of each course
- This helps us determine which courses are the prerequisites
- We make a BFS traversal
- The queue initially consists of all the courses with indegree 0 -- prerequisites
- At each prequisite, we find all the next courses and reduce their indegree count by 1
- At the same time we use a dist array to track the max amount of time we need to wait until we can start taking that course
- if indegree count of a course becomes 0, we add it to the queue
'''
def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    graph = defaultdict(list)
    inDegree = [0] * n
    for prv, nxt in relations:
        prv, nxt = prv - 1, nxt - 1  # convert into zero-based index
        graph[prv].append(nxt)
        inDegree[nxt] += 1

    q = deque([])
    dist = [0] * n
    for u in range(n):
        if inDegree[u] == 0:
            q.append(u)
            dist[u] = time[u]

    while q:
        u = q.popleft()
        for v in graph[u]:
            dist[v] = max(dist[u] + time[v], dist[v])  # Update `dist[v]` using the maximum dist of the predecessor nodes
            inDegree[v] -= 1
            if inDegree[v] == 0:
                q.append(v)
    return max(dist)