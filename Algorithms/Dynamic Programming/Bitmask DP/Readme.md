### The motivation behind Bitmask DP

Consider being given an array of integers.
arr = [1,2,3]

Consider generating all the subsequences/subsets of this array.

[]
[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]

There are 2^n subsequences possible for an array of size n

Consider space complexity for storing the subsets.
O(n*2^n)

Now consider masking every position in the array with a single bit.

This way, a single bit can tell us whether this element is included in our subset or not.

All we are storing therefore is an array of integer (whose bits determine the subsequence)

[]       - 000 - 0
[1]      - 001 - 1
[2]      - 010 - 2
[3]      - 100 - 4
[1,2]    - 011 - 3
[1,3]    - 101 - 5
[2,3]    - 110 - 6
[1,2,3]  - 111 - 7

Space complexity : O(2^n)