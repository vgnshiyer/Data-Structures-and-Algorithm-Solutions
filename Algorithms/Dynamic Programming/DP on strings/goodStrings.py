class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10 ** 9 + 7

        def kmp(pattern):
            n = len(pattern)
            j = 0
            lps = [0] * n

            for i in range(1, n):
                while j > 0 and pattern[i] != pattern[j]: j = lps[j - 1]
                if pattern[i] == pattern[j]: 
                    j += 1 ## longest suffix matched so far
                    lps[i] = j
            return lps
        
        lps = kmp(evil)

        @cache
        def dfs(i, prefS1, prefS2, evilLen):
            if evilLen == len(evil): return 0 # found evil substring (invalid string)
            if i == n: return 1 # found a good string

            start = s1[i] if prefS1 else 'a'
            end = s2[i] if prefS2 else 'z'
            ans = 0

            for c in range(ord(start), ord(end) + 1):
                ch = chr(c)
                j = evilLen ## number of chars in evil matched so far
                while j and evil[j] != ch: ## while current char does not match, go back in the pattern
                    j = lps[j - 1]
                if evil[j] == ch: j += 1 ## char matched, increase substring matched size

                ans += dfs(i + 1, prefS1 and (ch == s1[i]), prefS2 and (ch == s2[i]), j)
            return ans % mod

        return dfs(0, True, True, 0) % mod
