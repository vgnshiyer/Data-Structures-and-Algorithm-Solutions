from collections import defaultdict, deque

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = defaultdict(list)
    for from_, to, cost in flights:
        adj[from_].append((to, cost))
    
    queue = deque()
    queue.append((src, 0))
    dist = {}
    k += 1

    while queue and k:
        s = len(queue)
        while s:
            city, cost = queue.popleft()
            for nextcity, newcost in adj[city]:
                if nextcity not in dist or cost + newcost < dist[nextcity]:
                    dist[nextcity] = cost + newcost
                    ## made a mistake here. of adding all possible paths back to the queue
                    ## If a path is worse than the previously computed path, there is no point in going forward that path, since there are no negative edges in the graph.. 
                    queue.append((nextcity, cost + newcost))
            s -= 1
        k -= 1
    return dist.get(dst, -1)

## using bellman form (dynamic programming) -- view https://github.com/vgnshiyer/Data-Structures-and-Algorithm-Solutions/blob/main/Algorithms/Graph%20Algorithms/bellmanFord.cpp
def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    dp = [float('inf') for i in range(n)]
    dp[src] = 0

    for i in range(k + 1):
        dp_copy = dp.copy()
        for from_, to, price in flights:
            if dp[from_] + price < dp_copy[to]:
                dp_copy[to] = dp[from_] + price
        dp = dp_copy
    return dp[dst] if dp[dst] != float('inf') else -1
