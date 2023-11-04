'''
There can be at most k ^ n possible password combinations.

n = 3, (k choices) * (k choices) * (k choices)
We start with (n - 1) 0's. (There is no other better way that starting with this.. 
Try few examples: Start with 1s => 110100 (10 is repeated))

We maintain a visited set to make sure that each password combination is explored only once. This is like creating a eulerian tour where password combinations are edges in a graph.
'''
def crackSafe(self, n: int, k: int) -> str:
    self.password = ''
    seen = set()

    def dfs(s):
        if len(seen) == k ** n: 
            self.password = s
            return True

        prev = s[len(s) - n + 1:]
        for i in range(k):
            nxt = prev + str(i)
            if nxt not in seen:
                seen.add(nxt)
                if dfs(s + str(i)): return True
                seen.remove(nxt)
        return False

    dfs('0' * (n - 1))
    
    return self.password