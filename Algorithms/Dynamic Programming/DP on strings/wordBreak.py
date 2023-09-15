def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        state: dp[i] -> can the word be segmented from this position
        transition: dp[i] |= dp[j] if s[i:j+1] in wordDict
        base case: dp[n] = True
        '''
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                l = len(word)
                if s[i:i+l] == word:
                    dp[i] |= dp[i + l]

        return dp[0]