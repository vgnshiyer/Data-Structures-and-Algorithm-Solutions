class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        d = {}
        class point:
            def __init__(self, *args):
                self.x = args[0]
                self.y = args[1]

            def __sub__(self, other):
                return abs(self.x - other.x) + abs(self.y - other.y)

            def __str__(self):
                return f'{self.x}, {self.y}'

            def __lt__(self, other):
                return True

            def get(self):
                return (self.x, self.y)

        start = point(*start)
        target = point(*target)
        specialRoads = [[a, b, c, d, x] for a, b, c, d, x in specialRoads if x < abs(a - c) + abs(b - d)]

        heap = [(0, start)]
        while heap:
            c, i = heappop(heap)
            if i.get() not in d:
                d[i.get()] = c
                for road in specialRoads:
                    heappush(heap, (c + (point(*road[:2]) - i) + road[-1], point(*road[2:])))

        ans = start - target
        for road in specialRoads:
            b = point(*road[2:])
            ans = min(
                ans, d[b.get()] + (target - b)
            )

        return ans
