'''
Intuition
This problem is similar to the bst_sequences problem on leetcode. https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/

Most solutions here talk about placing n-th pair at available positions. But here, we will discuss an alternative solution that is much simpler to understand.

At n = 1, we only have one way to arrange pickups and deliveries.
P1D1

At n = 2, we have 4 places to arrange {P1, P2, D1, D2}
Consider them as separate pairs we want to arrange in 4 available places while maintaining the relative order of pickups and deliveries. This is the part that makes it similar to the bst_sequences problem.
left = [P1, D1], right = [P2, D2]
We need to find the number of ways we can interleave them while maintaining the relative order.

If we choose to arrange the elements in the left array at the available 4 positions, we can easily arrange elements in the right array.
Therefore ans = Comb(len(left) + len(right), len(left))

In this problem, the right array will always be of length 2. Why? Because at every i-th order we only have two elements to place {Pi, Di}.

Approach
First we start with our base case for n = 1, ans = 1.
We will loop from 2 to n.
At every i-th order, we calculate the total number of ways to arrange P's and D's using the below formula.
ans *= math.comb(i*2, 2)

'''

def countOrders(n: int) -> int:
    mod = 10 ** 9 + 7

    ans = 1
    for i in range(2, n + 1):
        ans *= math.comb(i*2, 2)
        ans %= mod
    return ans