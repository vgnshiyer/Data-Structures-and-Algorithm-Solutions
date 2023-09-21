class KMPSearch:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lps = self._compute_lps()

    def _compute_lps(self):
        m = len(self.pattern)
        lps = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and self.pattern[i] != self.pattern[j]: j = lps[j - 1]
            if self.pattern[i] == self.pattern[j]:
                j += 1
                lps[i] = j
        return lps

    def search(self, text):
        n = len(text)
        m = len(self.pattern)
        i = j = 0

        for i in range(n):
            while j > 0 and text[i] != self.pattern[j]: j = self.lps[j - 1]
            if text[i] == self.pattern[j]: j += 1
            if j == m: return i - m # pattern found
        return -1

if __name__ == '__main__':
    s = 'abcdeabcdf'
    p = 'abcdf'

    kmp_search = KMPSearch(p)
    result = kmp_search.search(s)

    if result != -1:
        print(f"Pattern found at index {result}")
    else:
        print("Pattern not found")
