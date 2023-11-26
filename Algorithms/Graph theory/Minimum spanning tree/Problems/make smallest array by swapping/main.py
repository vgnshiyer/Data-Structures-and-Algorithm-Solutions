class DSU:
    def __init__(self, nums):
        self.parent = {}
        for x in nums:
            self.parent[x] = x
        self.mp = defaultdict(list)

    def find(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[ self.parent[a] ]
            a = self.parent[a]
        return self.parent[a]

    def union(self, a, b):
        pb = self.find(b)
        self.parent[self.find(a)] = pb
        heappush(self.mp[pb], a)

    def get_min(self, a):
        pa = self.find(a)
        return heappop(self.mp[pa]) if self.mp[pa] else -1

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        n = len(nums)
        dsu = DSU(nums)
        dsu.union(sorted_nums[0], sorted_nums[0])

        for i in range(1, n):
            if sorted_nums[i] - sorted_nums[i - 1] <= limit:
                dsu.union(sorted_nums[i], sorted_nums[i - 1])
            else:
                dsu.union(sorted_nums[i], sorted_nums[i])

        for i in range(n):
            nums[i] = dsu.get_min(nums[i])

        return nums