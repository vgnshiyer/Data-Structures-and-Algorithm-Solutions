## Problem link: https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/description/

## Intuition:

- number of ways to arrange two subtrees of a node is `comb(n, n - r)`
- number of ways to arrange `t` subtrees is `comb(n, t1) * comb(n - t1, t2) * comb(n - t1 - t2, t3) * ... * comb(tn, tn)`

## Notes:

- state: `dp[i]` --> number of ways to arrange dependant rooms at this room
- transition: `dp[i] = dp[t1] * dp[t2] * ... * dp[tn] * (comb(n, t1) * comb(n - t1, t2) * comb(n - t1 - t2, t3) * ... * comb(tn, tn))`
- base case: dp[i] = 1