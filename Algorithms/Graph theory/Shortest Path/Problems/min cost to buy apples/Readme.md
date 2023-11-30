## Problem link: https://leetcode.ca/2022-12-31-2473-Minimum-Cost-to-Buy-Apples/

## Intuition:

- The best cost to reach a node and come back is traversing the shortest path twice

## Notes:

- Perform djikstra for each node to get the all pair shortest path O(n ^ 2 log n)