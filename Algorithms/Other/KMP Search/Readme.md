### KMP Search

Knuth-Morris-Pratt algorithm is a pattern matching algorithm that searches the occurrences of a word within a given string. The main gist of the algorithm is to avoid repeated comparisons by looking at the pattern to determine where to start the next match on a particular mismatch with the main string. Basically it will try to see if a suffix of the pattern matched so far is already present as a prefix in the same area. If so, it will avoid comparing the prefix again and begin the search from the next character.

The key observation made in this algorithm is that a suffix present as a prefix in the pattern can be skipped.

**Intuition**:

```
Naive algorithm: O(n * m) Time.
Given an string: abcdabcdf
and a pattern: abcdf

We start from i = 0, j = 0
while s[i] == p[j]: i++, j++

abcdabcdf
    i
abcdf
    j

When we find a mismatch, we reset i back to 0 and j to 1.
Basically we have a window of size len(pattern) and we move the window forward until we find the pattern. This is a waste of time as the pattern is being matched again and again.
```

The main difference between the naive and KMP search is that we do not go back in the main string.

**Algorithm**:

1. Create a temporary array (known as pi or lps or longest prefix suffix) which answers the query of whether a suffix of the pattern matched so far is present as a prefix. --> O(n) time
2. Now start matching the main string and the pattern.
3. On a mismatch, more `j` in pattern to `pattern[temp[j-1]]`
4. Continue comparing.
5. If we reach the end in both strings, we have found the pattern.
