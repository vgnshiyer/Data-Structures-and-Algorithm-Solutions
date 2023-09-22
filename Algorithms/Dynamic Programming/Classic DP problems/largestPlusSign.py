def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    mines = set((x, y) for x, y in mines)
    left = [[0] * n for _ in range(n)]
    right = [[0] * n for _ in range(n)]
    up = [[0] * n for _ in range(n)]
    down = [[0] * n for _ in range(n)]

    for i in range(n):
        l = 0
        for j in range(n): 
            if (i, j) in mines: l = -1
            l += 1
            left[i][j] = l
    
    for i in range(n):
        r = 0
        for j in range(n - 1, -1, -1):
            if (i, j) in mines: r = -1
            r += 1
            right[i][j] = r

    for j in range(n):
        u = 0
        for i in range(n):
            if (i, j) in mines: u = -1
            u += 1
            up[i][j] = u

    for j in range(n):
        d = 0
        for i in range(n - 1, -1, -1):
            if (i, j) in mines: d = -1
            d += 1
            down[i][j] = d

    best = 0
    for i in range(n):
        for j in range(n):
            if (i, j) in mines: continue
            u = up[i - 1][j] if i else 0
            d = down[i + 1][j] if i < n - 1 else 0
            l = left[i][j - 1] if j else 0
            r = right[i][j + 1] if j < n - 1 else 0
            
            best = max(best, 1 + min([u, d, l, r]))
    return best