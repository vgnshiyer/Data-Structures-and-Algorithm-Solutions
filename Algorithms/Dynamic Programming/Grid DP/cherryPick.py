'''
Initial approach I had for this problem: 
- Do a normal traversal from 0,0 to n-1,m-1 while picking the maximum number of cherries along the path.
- As we are building the optimal path with maximum cherries, remove the cherry from the position from the grid.
- At the end, do a reverse traversal from n-1, m-1 to 0,0, running the same algorithm.
- Return the sum of the two traversals.

Problem with this approach:
- This approach considers the optimal path for one particular traversal.
- But not for the whole round trip. 
- So for the second reverse traversal, we could have taken a different path than the local optimal path, which would have given us the global optimal path.

Instead of treating these traversals as one after the other, we can denote them as one by putting two people making the traversal simultaneously.
'''

def cherryPickup_recursive(grid: List[List[int]]) -> int:
    n = len(grid)

    dp = {}
    def getMaxCherries(r1, c1, r2, c2):
        if r1 == n or c1 == n or r2 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1: return -float('inf')
        if r1 == n - 1 and c1 == n - 1: return grid[r1][c1]

        if r1 == r2 and c1 == c2: cherries = grid[r1][c1]
        else: cherries = grid[r1][c1] + grid[r2][c2]

        if (r1, c1, r2, c2) not in dp:
            dp[(r1, c1, r2, c2)] = cherries + max(
                getMaxCherries(r1, c1 + 1, r2, c2 + 1),
                getMaxCherries(r1 + 1, c1, r2 + 1, c2),
                getMaxCherries(r1, c1 + 1, r2 + 1, c2),
                getMaxCherries(r1 + 1, c1, r2, c2 + 1)
            )
        return dp[(r1, c1, r2, c2)]

    return max(0, getMaxCherries(0, 0, 0, 0))

'''
We can reduce the space complexity by making a key observation here.
Note that r1 + c1 = r2 + c2 for all the cells that are on the same diagonal.

therefore c2 can be expressed as c2 = r1 + c1 - r2.
Hence space complexity can be O(n ^ 3)
'''

def cherryPickup(grid: List[List[int]]) -> int:
    n = len(grid)

    dp = {}
    def getMaxCherries(r1, c1, r2):
        c2 = r1 + c1 - r2
        if r1 == n or c1 == n or r2 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1: return -float('inf')
        if r1 == n - 1 and c1 == n - 1: return grid[r1][c1]

        if r1 == r2 and c1 == c2: cherries = grid[r1][c1]
        else: cherries = grid[r1][c1] + grid[r2][c2]

        if (r1, c1, r2) not in dp:
            dp[(r1, c1, r2)] = cherries + max(
                getMaxCherries(r1, c1 + 1, r2),
                getMaxCherries(r1 + 1, c1, r2 + 1),
                getMaxCherries(r1, c1 + 1, r2 + 1),
                getMaxCherries(r1 + 1, c1, r2)
            )
        return dp[(r1, c1, r2)]

    return max(0, getMaxCherries(0, 0, 0))
