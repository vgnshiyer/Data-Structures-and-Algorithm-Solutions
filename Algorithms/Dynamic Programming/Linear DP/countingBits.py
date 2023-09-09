'''
0000 -> 0
0001 -> 1 
0010 -> 1
0011 -> 2
0100 -> 1
0101 -> 2
...

if i is even, dp[i] = dp[i//2]
if i is odd, dp[i] = dp[i-1] + 1
'''
def countBits(n: int) -> list[int]:
    if n == 0: return [0]
    res = [0] * (n+1)

    for i in range(1, n + 1):
        if i & 1:
            res[i] = res[i-1] + 1
        else:
            res[i] = res[i // 2]
    return res