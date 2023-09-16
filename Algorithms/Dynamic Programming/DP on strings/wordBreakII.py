def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    sentences = []

    def dfs(i, sentence=''):
        if i >= len(s):
            sentences.append(sentence.strip())
            return

        for word in wordDict:
            if s[i:i + len(word)] == word:
                dfs(i + len(word), sentence + ' ' + word)
    
    dfs(0)
    return sentences

def wordBreak_optimized(s: str, wordDict: List[str]) -> List[str]:
    sentences = []
    memo = {}

    def dfs(i):
        if i >= len(s): return ['']

        if i not in memo:
            res = []
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    rest = dfs(i + len(word))
                    for w in rest:
                        res.append((word + ' ' + w).strip())
            memo[i] = res
        return memo[i]
    
    return dfs(0)