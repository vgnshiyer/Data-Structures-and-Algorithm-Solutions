## Problem link: https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

## Intuition:

- Think about the problem without the time constraint.
- Simple Djikstra.
- Including the time is easy. --> Just add a node when you reach it quicker than before.

## Notes:

- Use a hashmap to track reaching time for each node.
- Sort priority queue by minimum cost.