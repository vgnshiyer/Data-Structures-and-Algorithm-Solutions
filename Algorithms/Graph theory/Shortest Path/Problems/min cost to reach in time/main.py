class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)

        adj = defaultdict(list)
        for i, j, t in edges:
            adj[i].append((j, t))
            adj[j].append((i, t))

        pq = [(passingFees[0], 0, 0)]
        time = {}

        while pq:
            f, i, t = heappop(pq)

            if t > maxTime: continue

            if i == n - 1: return f

            '''
            there might be a path which may cost more or the same but takes less time --> might be the one which helps us reach our destination
            '''
            if i not in time or time[i] > t:
                time[i] = t
                for j, tj in adj[i]:
                    heappush(pq, (f + passingFees[j], j, t + tj))

        return -1