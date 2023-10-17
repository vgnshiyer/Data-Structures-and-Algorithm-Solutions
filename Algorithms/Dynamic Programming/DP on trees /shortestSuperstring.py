## This problem was a nice introduction to the travelling salesman problem
'''
We consider the words as nodes and the length of non-overlapping string as our cost. We need to find a path which covers all nodes with minimal cost. We use a mask to represent all the words which have been picked so far. Along with that we also keep track of the previous element picked. 
'''
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlap = [[''] * n for _ in range(n)]

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
            if mask == ((1 << n) - 1): return ''
            if (prev, mask) in dp: return dp[(prev, mask)]
            ans = '*' * 1000000
            for i in range(n):
                if mask & (1 << i): continue
                word = overlap[prev][i] if prev != -1 else words[i]
                ans = min(ans, word + TSP(i, mask | (1 << i), dp), key=len)
            dp[(prev, mask)] = ans
            return ans

        return TSP(-1, 0, {})