def distinctSubseqII(self, s: str) -> int:
    '''
    state: dp[i] = number of subsequences that end at char i (i belongs to [1,26])
    transition: dp[i] = sum(dp[i] + 1)
    eg. current subsequences {a, ab, b}.. new letter 'c'
    possible subsequences = {ac, abc, bc} + 1 (c) 
    '''
    dp = [0] * 26
    mod = 10 ** 9 + 7

    for c in s:
        dp[ord(c) - ord('a')] = sum(dp) % mod + 1
    return sum(dp) % mod