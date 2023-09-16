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