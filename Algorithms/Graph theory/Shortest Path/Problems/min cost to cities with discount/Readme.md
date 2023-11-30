## Problem link: https://leetcode.ca/2021-12-16-2093-Minimum-Cost-to-Reach-City-With-Discounts/

## Intuition:

- At any city with discounts d left, we have 2 options
    1. use the discount
    2. keep the discount

## Notes:

- Mistake: I maintained the same distance array for all discounts. 
    - This made the algorithm too greedy --> Meaning it was trying to find the shortest immediate path by readily using the discount. 
    - This also resulted in comparing a discounted path with a non discounted path
    (d[i][dis] -- d[i][dis - 1])
- Both the node and the number of discounts need to be maintained in the state (distance array)