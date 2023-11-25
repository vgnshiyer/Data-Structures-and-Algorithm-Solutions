## Problem link: https://leetcode.com/problems/count-pairs-of-nodes/description/

## Intuition:

- we can count the number of pairs that exceed q, and think of removing invalid pairs (based on removing extra edges) later.
- Only those edges are invalid whose `deg[x] + deg[y] - adj[x][y] <= q`.

## Notes:

- Binary search implementation in this solution is amazing which counts the number of pairs which are greater than the target. 

Credits: https://leetcode.com/problems/count-pairs-of-nodes/solutions/1096740/c-java-python3-two-problems-o-q-n-e/