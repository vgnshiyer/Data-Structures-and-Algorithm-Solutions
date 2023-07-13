'''
Find number of ways to form k groups from n people such that a group has greater than equal to the number of people in the groups to its left.

eg. n = 8, k = 4
ans = {
    [1,1,1,5], [1,1,2,4], [1,1,3,3], [2,2,2,2], [1,2,2,3]
} = 5
'''

from functools import cache

def nToKGroups(n, m):
    @cache
    def helper(n, m, p):
        if n == 0 and m == 0: return 1
        if n <= 0 or m <= 0: return 0

        res = 0
        for i in range(p, 0, -1):
            res += helper(n-i, m-1, i)
        return res
    
    return helper(n, m, n)

if __name__ == '__main__':
    print(nToKGroups(8,4)) ## 5
    print(nToKGroups(200,20)) ## 87438760128