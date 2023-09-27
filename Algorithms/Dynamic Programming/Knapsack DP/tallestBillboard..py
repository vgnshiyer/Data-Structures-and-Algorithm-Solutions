def tallestBillboard(rods: List[int]) -> int:
    dp = [[-1] * 10001 for _ in range(21)]

    def getTallestSupportLength(i, lenDiff):
        if i >= len(rods): 
            if lenDiff == 0: return 0
            else: return -float('inf')
        
        if dp[i][lenDiff] != -1: return dp[i][lenDiff]
        
        leaveCurrentRod = getTallestSupportLength(i + 1, lenDiff)
        '''
        Notice that we only add rods[i] for support 1. As we want tallest support length for one of the supports. Adding it in both would give us the total length of both supports. 
        '''
        attachToSupport1 = rods[i] + getTallestSupportLength(i + 1, lenDiff + rods[i])
        attachToSupport2 = getTallestSupportLength(i + 1, lenDiff - rods[i])
        
        dp[i][lenDiff] = max([leaveCurrentRod, attachToSupport1, attachToSupport2])

        return dp[i][lenDiff]

    return getTallestSupportLength(0, 0)