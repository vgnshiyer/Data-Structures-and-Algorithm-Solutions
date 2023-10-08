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
    '''
        we have v places to move downwards and h places to move right.
        There are total nCv combinations of paths, where n = h + v

        We pick characters one by one. 
        - If we pick an 'h', we will have left h-1 and v moves to take.
        - We will have C(h - 1 + v, v) paths left. If this number is greater than k, it means that our kth path is in this range. Therefore we must pick h here. 
        - If that number is less than k, it means we have gone past our required string. We meed to come back c combinations. We keep doing this until we reach k == 0 which is our desired string.
    '''
    v, h = destination
    n = v + h
    res = ''
    for i in range(n):
        paths = comb(n - i - 1, v)
        if paths >= k: ## our kth path is in this range
            res += 'H' ## we select H
        else: ## we have gone past our required string
            res += 'V' ## we select V
            v -= 1
            k -= paths ## we need to come back c combinations
    return res
        