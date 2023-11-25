class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        adj = defaultdict(int)
        deg = [0] * (n + 1)
        
        for i, j in edges:
            # count all valid pairs
            adj[(min(i, j), max(i, j))] += 1
            deg[i] += 1
            deg[j] += 1

        ans = [0] * len(queries)
        sorted_deg = sorted(deg)

        for i, q in enumerate(queries):
            '''
            For a range l, r where q = 2 and s[l] = 2, s[r] = 3
            l = 1, r = 3
            [2,2,3]
            We can add pairs {(2, 2), (2, 3)} --> (3 - 1) = 2

            Next iteration, we narrow down be receding r.

            On the other hand, if the sum <= q, we advance l
            '''
            l, r = 1, n
            while l < r:
                if q < sorted_deg[l] + sorted_deg[r]:
                    ans[i] += r - l
                    r -= 1
                else: l += 1

            # remove all pairs which become lesser than q once the double counted edges are removed
            for x, y in adj:
                if x >= y: continue
                if q < deg[x] + deg[y] and deg[x] + deg[y] - adj[(x, y)] <= q:
                    ans[i] -= 1

        return ans