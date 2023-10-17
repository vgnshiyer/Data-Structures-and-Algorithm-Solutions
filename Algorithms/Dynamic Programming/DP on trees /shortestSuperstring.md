https://leetcode.com/problems/find-the-shortest-superstring/solutions/4179688/easy-to-understand-tsp-implementation-top-down-bottom-up-python/
# Approach
<!— Describe your approach to solving the problem. —>
Consider this problem as a graph problem where we need to visit every single node with the minimal overall cost. The words will be our nodes and the nonOverlapping substring between two words will be our cost.

# Complexity
- Time complexity:
<!— Add your time complexity here, e.g. $$O(n)$$ —>
$$O(n^2 * 2^n)$$

- Space complexity:
<!— Add your space complexity here, e.g. $$O(n)$$ —>
$$O(n * 2^n)$$

# Code

### Easy to understand - Top-Down DP
```
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlap = [[‘’] * n for _ in range(n)]

        def getOverlap(a, b):
            l, i = 0, 1
            while i <= min(len(a), len(b)):
                if a[len(a)-i:] == b[:i]:
                    l = i
                i += 1
            return b[l:]

        for i in range(n):
            for j in range(n):
                if i != j: overlap[i][j] = getOverlap(words[i], words[j])

        def TSP(prev, mask, dp):
            if (prev, mask) in dp: return dp[(prev, mask)]
            if mask == ((1 << n) - 1): return ‘’
            ans = ‘*’ * 1000000
            for i in range(n):
                if mask & (1 << i): continue
                word = overlap[prev][i] if prev != -1 else words[i]
                ans = min(ans, word + TSP(i, mask | (1 << i), dp), key=len)
            dp[(prev, mask)] = ans
            return ans

        return TSP(-1, 0, {})
```

### Bottom-Up DP
Notice here that we apply a push-dp instead of a pull-dp. That is because, there is no way for us to know in advance what the best string would be for a mask (7) or (111) where all the strings will be included where n = 3.

Therefore we start with a base case where only one string will be included and we build our dp by pushing values forward in the mask.

Finally, we get the minimum string with all words included (mask = ($$2^n - 1$$))
```
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlap = [[‘’] * n for _ in range(n)]

        def getOverlap(a, b):
            l, i = 0, 1
            while i <= min(len(a), len(b)):
                if a[len(a)-i:] == b[:i]:
                    l = i
                i += 1
            return b[l:]

        for i in range(n):
            for j in range(n):
                if i != j: overlap[i][j] = getOverlap(words[i], words[j])
        ans = ‘*’ * (10**4)
        dp = [[ans] * (1 << n) for _ in range(n)]
        for i in range(n): dp[i][(1 << i)] = words[i]

        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    for j in range(n):
                        if i != j and mask & (1 << j): continue
                        dp[j][mask | (1 << j)] = min(dp[j][mask | (1 << j)], dp[i][mask] + overlap[i][j], key=len)

        for i in range(n): ans = min(ans, dp[i][(1 << n) - 1], key=len)
        return ans
```