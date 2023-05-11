## Segment trees

A segment tree is a data structure that stores information about the array intervals as a tree. This allows answering range queries over an array efficiently, while still being flexible enough to allow quick modification of the array. This includes finding the sum over a range in the array, finding the min/max among a range of elements, all in O(logn)(hieght of the tree is log n) time.

Now a prefix sum algorithm can handle range queries in O(1) time if the values are precomputed. However, if the values are updated, it takes O(n) to recompute the prefix sums.

