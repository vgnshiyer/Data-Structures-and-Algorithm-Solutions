"""
The maze problem

Given a maze of size m,n find ways to solve the reach m-1,n-1 from 0,0 block.
Note that u can only move right or down. No diagonal, left or up movement.

RECURSION + BACKTRACKING

for every i,j, we calculate solutions(i,j+1) + solutions(i+1,j)
"""
def solveMaze(i,j, n, m):
    
    if i == n or j == m: return 0
    if i == n-1 and j == m-1: return 1
    
    return solveMaze(i,j+1,n,m) + solveMaze(i+1,j,n,m)

if __name__ == "__main__":
    print(solveMaze(0,0,3,3))