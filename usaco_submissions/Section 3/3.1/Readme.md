### USACO
##### Section 2.4 Solutions

**Problem 1.** AgriNet

**Approach:**
A simple MST problem which asks the minimum lenght of a value to connect the entire graph. We can either use Union-Find(Kruskals) or Prims algorithm to find the reqd value.

**Problem 2.** Score Inflation

**Approach:**
This is a classic 0-1 Knapsack type problem where we want to maximize the points within the given time limit.
state: dp[i][j] => max points that can be scored given j as deadline 
transition: dp[i][j] = max(dp[i-1][j], points[i] + dp[i][j - minutes[i]])
base case: dp[anything][0] = 0;

Here, we notice that we only need the previous row and other rows are superfluous to be stored throughout the entire calculation. This gives room for some space optimization. Refer the code.

**Problem 3.** Humble Numbers

**Approach:**
Earlier I tried to run a loop from 1 to a really large number, counting the humble numbers I find by checking if the current number is fully divisible by the available primes. This is definetely SLOWER.

Faster approach is to generate the humble number one by one.
At every step we try to find the minimum humble number greater than the previous humble number.
 --> Earlier I created a O(n*n*k) solution, which tried all possible combinations of prime factors and previous humble numbers. Again ended up in TLE.
An important thing I noticed was I was making pointless computations after a certain point because some older combinations were always smaller than the previous humble number.
Having an auxiliary array for maintaining the best index for each prime factor, made the algorithm much faster.