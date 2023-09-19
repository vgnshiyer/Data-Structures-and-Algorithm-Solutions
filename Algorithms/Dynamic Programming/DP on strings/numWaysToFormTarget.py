'''
### A Very silly mistake. 

```
if i >= n and j >= m: return 1
// It is not required to reach the end in index i. 

Just reaching the end in index j is enough. 
if j >= m: return 1
```
'''

def numWays(words: List[str], target: str) -> int:
    mod = 10 ** 9 + 7
    n = len(words[0]) ## length of words
    m = len(target)

    mp = [defaultdict(int) for _ in range(n)]
    for word in words:
        for i in range(n):
            mp[i][word[i]] += 1

    @cache
    def dfs(i, j):
        if j >= m: return 1
        if i >= n: return 0
        return (dfs(i + 1, j) % mod + (mp[i][target[j]] * dfs(i + 1, j + 1) if target[j] in mp[i] else 0) % mod) % mod

    return dfs(0, 0) % mod