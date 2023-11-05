## cheapest flights with k stops


def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    dist = [inf] * n
    adj = defaultdict(list)
    for from_, to, cost in flights:
        adj[from_].append((to, cost))

    queue = deque([(src, 0)])

    k += 1
    while queue and k:
        l = len(queue)
        while l:
            city, cost = queue.popleft()

            for to, costTo in adj[city]:
                if cost + costTo < dist[to]:
                    dist[to] = cost + costTo
                    queue.append((to, dist[to]))
            l -= 1
        k -= 1

    return dist[dst] if dist[dst] < inf else -1