def isPrintable(grid: List[List[int]]) -> bool:
    n, m = len(grid), len(grid[0])
    
    class color:
        def __init__(self, c, topleft, bottomright):
            self.c = c
            self.topleft = topleft
            self.bottomright = bottomright

        def updateTopLeft(self, temp):
            self.topleft = (min(self.topleft[0], temp[0]), min(self.topleft[1], temp[1]))

        def updateBottomRight(self, temp):
            self.bottomright = (max(self.bottomright[0], temp[0]), max(self.bottomright[1], temp[1]))

        def getBounds(self):
            return self.topleft[0], self.topleft[1], self.bottomright[0], self.bottomright[1]

    colors = {}
    for i in range(n):
        for j in range(m):
            c = grid[i][j]
            if c not in colors:
                colors[c] = color(c, (i, j), (i, j))
            else:
                colors[c].updateTopLeft((i, j))
                colors[c].updateBottomRight((i, j))

    def test(col):
        a, b, c, d = col.getBounds()
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                if grid[i][j] > 0 and grid[i][j] != col.c:
                    return False

        for i in range(a, c + 1):
            for j in range(b, d + 1):
                grid[i][j] = 0
        return True

    while colors:
        colors2 = {}
        for c in colors:
            if not test(colors[c]):
                colors2[c] = colors[c]
        if len(colors) == len(colors2): return False
        colors = colors2
    return True