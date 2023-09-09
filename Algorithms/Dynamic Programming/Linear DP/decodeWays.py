def numDecodings(s: str) -> int:
    '''
    state: dp[i] -> number of ways to decode from position i
    transition: dp[i] += dp[i-1] if s[i] != 0 ; dp[i] += dp[i-2] if s[i-1:i+1] <= 26
    base: dp[0] = 1
    '''
    def valid(num):
        if num[0] == '0': return False
        return int(num) > 0 and int(num) <= 26

    cur, minusOne, minusTwo = 0, 1, None
    for i in range(0, len(s)):
        cur = 0
        if valid(s[i]): cur += minusOne
        if i and valid(s[i-1:i+1]): cur += minusTwo

        minusTwo = minusOne
        minusOne = cur
    return cur