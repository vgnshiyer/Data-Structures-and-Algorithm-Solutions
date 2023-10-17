'''
Given strings A and B, find the maximum overlapping substring of B in A.

eg. A = 'cat', B = 'attribute'

ans = 'cattribute'
'''

def getNonOverlap(a, b):
    n, m = len(a), len(b)
    
    l = 0
    for i in range(n):
        if a[n-i:] == b[:i]:
            l = i
            break
    return b[l:]  