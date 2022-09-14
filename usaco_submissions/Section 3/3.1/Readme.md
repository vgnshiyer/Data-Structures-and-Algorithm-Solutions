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