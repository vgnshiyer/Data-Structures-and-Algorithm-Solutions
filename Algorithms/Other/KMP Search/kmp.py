class KMPSearch:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lps = self._compute_lps()

    def _compute_lps(self):
        m = len(self.pattern)
        lps = [0] * m
        i, j = 0, 1

        while j < m:
            if self.pattern[i] == self.pattern[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]
        return lps

    def search(self, text):
        n = len(text)
        m = len(self.pattern)
        i = j = 0

        while i < n:
            if text[i] == self.pattern[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = self.lps[j - 1]

            if j == m:
                return i - m  # Pattern found at index i - m
        return -1  # Pattern not found

if __name__ == '__main__':
    s = 'abcdeabcdf'
    p = 'abcdf'

    kmp_search = KMPSearch(p)
    result = kmp_search.search(s)

    if result != -1:
        print(f"Pattern found at index {result}")
    else:
        print("Pattern not found")
