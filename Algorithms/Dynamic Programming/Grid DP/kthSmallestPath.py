## TLE Brute Force Solution
def kthSmallestPath(destination: List[int], k: int) -> str:
    @cache
    def dfs(i, j):
        if [i, j] == destination: return ['']

        paths = []

        toRight = dfs(i, j + 1) if j < destination[1] else []
        toBottom = dfs(i + 1, j) if i < destination[0] else []

        for p in toRight: paths.append('H' + p)
        for p in toBottom: paths.append('V' + p)

        return paths

    return dfs(0, 0)[k-1]

def kthSmallestPath_Optimized(destination, k):
    v, h = destination
    n = v + h
    res = ''
    for i in range(n):
        paths = comb(n - i - 1, v)
        if paths >= k:
            res += 'H'
        else:
            res += 'V'
            v -= 1
            k -= paths
    return res
        