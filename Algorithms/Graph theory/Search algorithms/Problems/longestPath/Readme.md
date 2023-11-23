## Problem link: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/

## Intuition:

- At every node we have 2 options.
    - Either include the current node in the longest path along with a path from the left and a path from the right.
    - Ignore the path via the node and include the parent in the longest path. 
- We take the maximum and return the path which includes a node's parent in the longest path.

## Notes:

- An important thing to note is that adjacent similar chars must be excluded from the longest path.
- If a node has a char equal to its parent (adjacent), we do not consider the path from that node.
