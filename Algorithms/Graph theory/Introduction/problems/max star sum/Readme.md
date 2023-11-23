## Problem link: https://leetcode.com/problems/maximum-star-sum-of-a-graph/

## Intuition:

- Key point to notice here is we need at most k nodes from a start node
- Therefore we must take the ones with most vals

## Notes: 

- Make sure to ignore edges with nodes that have negative value
- Becase, in our implementation, we directly add the sum of at most k nodes from a center
    - This might include a negative value node 
    - While we can make sure to record max at every update of the sum but ignoring negative values make the code look cleaner
