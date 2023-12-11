class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        f = Counter(nums) # O(n)
        f = [(k_, v) for k_, v in f.items()]

        def quick_select(left, right):
            pivot = right
            l, r = left, right
            i = l
            for j in range(l, r):
                if f[j][1] >= f[pivot][1]:
                    f[i], f[j] = f[j], f[i]
                    i += 1
            f[i], f[r] = f[r], f[i]

            # we keep sorting in descending order until our pivot is an element at position k
            if i + 1 == k: return f[:i + 1]
            elif i + 1 < k: return quick_select(i + 1, right)
            else: return quick_select(left, i - 1)

        return [c[0] for c in quick_select(0, len(f) - 1)]
