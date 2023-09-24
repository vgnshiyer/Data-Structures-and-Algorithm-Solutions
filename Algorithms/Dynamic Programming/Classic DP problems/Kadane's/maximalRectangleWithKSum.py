def maxSumSubmatrix(matrix):
    n, m = len(matrix), len(matrix[0])

    best = -float('inf')
    for l in range(m):
        rowSums = [0] * n
        for r in range(l, m):
            for i in range(n): rowSums[i] += matrix[i][r]

            colSums = [0]
            colSum = 0

            for rowSum in rowSums:
                colSum += rowSum
                diff = ColSum - k

                idx = bisect_left(colSums, diff)

                if idx < len(colSums): best = max(best, colSum - colSums[idx])
                insort(colSums, colSum)
    return best