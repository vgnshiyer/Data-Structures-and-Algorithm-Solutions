def isSubsequence(s: str, t: str) -> bool:
    j = 0
    for i in range(len(t)):
        if j == len(s): break
        if s[j] == t[i]: j += 1
    return j == len(s)