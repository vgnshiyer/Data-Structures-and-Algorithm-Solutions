def checkRecord(n: int) -> int:
    '''
    we divide the problem into multiple states
    // state[0] : end with A
    // state[1] : end with P and 0 A before end;
    // state[2] : end with P and 1 A before end;
    // state[3] : end with 1 L and 0 A before end;
    // state[4] : end with 1 L and 1 A before end;
    // state[5] : end with 2 L and 0 A before end;
    // state[6] : end with 2 L and 1 A before end;

    transtion:
    state[0] = state[1] + state[3] + state[5]
    state[1] = state[1] + state[3] + state[5]
    state[2] = state[0] + state[2] + state[4] + state[6]
    state[3] = state[1]
    state[4] = state[0] + state[2]
    state[5] = state[3]
    state[6] = state[4]

    base: state = [1(A), 1(P), 0, 1(L), 0, 0, 0] -> number of ways with length = 1
    '''

    mod = 10**9 + 7
    dp = [1, 1, 0, 1, 0, 0, 0]

    for i in range(2, n + 1):
        cur = [0] * 7
        cur[0] = ((dp[1] + dp[3]) % mod + dp[5]) % mod
        cur[1] = cur[0]
        cur[2] = (((dp[0] + dp[2]) % mod + dp[4]) % mod + dp[6]) % mod
        cur[3] = dp[1]
        cur[4] = (dp[0] + dp[2]) % mod
        cur[5] = dp[3]
        cur[6] = dp[4]

        dp = cur

    total_records = 0
    for r in dp: total_records = (total_records + r) % mod

    return total_records