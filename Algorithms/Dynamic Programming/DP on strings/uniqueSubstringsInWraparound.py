def uniqueSubstrings(s):
    '''
    ##### Mistakes I made
    - Was trying to use the formula of calculating the substrings based on the formula `n * n + 1 // 2`
    - Was interpreting the state as longest substring starting at position i.
    - where as I should have considered max number of substrings ending at position i.

    ##### Approach
    - initialize every single char in the array in a hashmap with max substring from that letter to 1
    - have a var `l=1`
    - for every `s[i] == s[i-1], l++`
    - if not equals `l = 1`
    - start a new substring
    - in the end, add all the lengths

    state: dp[l] = max number of substrings ending with letter l
    {a} + {b} = {b, ab} !! Notice that we do not include {a}, as it does not end with b
    transition: dp[l] = max(dp[l], dp[l] + 1) if s[i] == s[i-1] else 1
    base case: dp for all letters is 1
    '''

    res = {i:1 for i in s}
    l = 1
    for i in range(1, len(s)):
        a, b = s[i-1], s[i]
        l = l + 1 if (ord(b) - ord(a)) % 26 == 1 else 1
        res[b] = max(res[b], l)
    return sum(res.values())