def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    n, m = len(matrix), len(matrix[0])
    ans = 0

    for l in range(m):
        rowSums = [0] * n
        for r in range(l, m):
            for i in range(n): rowSums[i] += matrix[i][r]

            colSum = 0
            d = defaultdict(int)
            d[0] = 1

            for rowSum in rowSums:
                colSum += rowSum
                diff = colSum - target
                ans += d[diff]
                d[colSum] += 1
    return ans