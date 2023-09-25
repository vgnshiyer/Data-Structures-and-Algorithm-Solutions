def shortestCommonSupersequence(s1: str, s2: str) -> str:
    n, m = len(s1), len(s2)

    dp = [[''] * (m + 1) for _ in range(n + 1)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s1[i] == s2[j]: dp[i][j] = s1[i] + dp[i + 1][j + 1]
            else: dp[i][j] = max(dp[i + 1][j], dp[i][j + 1], key=len)
    
    lcs = dp[0][0]

    i, j = 0, 0
    res = ''
    for c in lcs:
        while i < n and s1[i] != c: 
            res += s1[i]
            i += 1

        while j < m and s2[j] != c:
            res += s2[j]
            j += 1
        i, j = i + 1, j + 1
        res += c
    return res + s1[i:] + s2[j:]