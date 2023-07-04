## Dynamic Programming

#### ​Those who don't remember the past, are condemned to repeat it. ~~Dynamic Programming

Dynamic programming is a technique that combines the correctness of complete search and the efficiency of greedy algorithms. Dynamic programming can be applied if the problem can be divided into overlapping subproblems that can be solved independently.

There are two uses for dynamic programming:
1. Finding an optimal solution: We want to find a solution that is as large as possible or as small as possible.
2. Counting the number of solutions: We want to calculate the total number of possible solutions.

**Memoization, Tabulation**
There are at least two main techniques of dynamic programming which are not mutually exclusive:

**Memoization (Top-Down Approach)** - This is a laissez-faire approach: You assume that you have already computed all subproblems and that you have no idea what the optimal evaluation order is. Typically, you would perform a recursive call (or some iterative equivalent) from the root, and either hope you will get close to the optimal evaluation order, or obtain a proof that will help you arrive at the optimal evaluation order. You would ensure that the recursive call never recomputes a subproblem because you cache the results, and thus duplicate sub-trees are not recomputed.

**example**: If you are calculating the Fibonacci sequence fib(100), you would just call this, and it would call fib(100)=fib(99)+fib(98), which would call fib(99)=fib(98)+fib(97), ...etc..., which would call fib(2)=fib(1)+fib(0)=1+0=1. Then it would finally resolve fib(3)=fib(2)+fib(1), but it doesn't need to recalculate fib(2), because we cached it.
This starts at the top of the tree and evaluates the subproblems from the leaves/subtrees back up towards the root.


**Tabulation (Bottom-Up Approach)** - You can also think of dynamic programming as a "table-filling" algorithm (though usually multidimensional, this 'table' may have non-Euclidean geometry in very rare cases*). This is like memoization but more active, and involves one additional step: You must pick, ahead of time, the exact order in which you will do your computations. This should not imply that the order must be static, but that you have much more flexibility than memoization. 

**example**: If you are performing fibonacci, you might choose to calculate the numbers in this order: fib(2),fib(3),fib(4)... caching every value so you can compute the next ones more easily. You can also think of it as filling up a table (another form of caching).
Before running the algorithm, the programmer considers the whole tree, then writes an algorithm to evaluate the subproblems in a particular order towards the root, generally filling in a table.

**Pros and Cons**
* Memoization is easy to code. 
* Iterative tabulation method is chosen by most programmers, as it makes the code short. Although it may not be as easy as the recursive function to code.
* Note: both top-down and bottom-up approach can be written with recursive or iterative tabular method(although may not seem natural).
* With memoization, if the recursion tree is very deep(eg. fin(10^6)) it may result in a stack overflow because of delayed computation.
* It is easier to perform space optimization with an iterative approach. 
* A con of tabulation method is that we may end up calculating values that may be unnecessary. 
(eg. To calculate 5C3 in binomial coefficiants, we might end up calculating a lot of values that we may not need for getting 5C3)

## What to think of before approaching a dp problem:
The **state-transition-base** method.
* determine the state of your dp. eg. dp[n] for a function say fibonacci.
* determine the transition. How are consecutive subproblems solved based on values of previous problems.
For eg. in case of Fibonacci, f(n) = f(n-1) + f(n-2)
* Smallest subproblem. (Base Case) f(0) = 0, f(1) = 1.