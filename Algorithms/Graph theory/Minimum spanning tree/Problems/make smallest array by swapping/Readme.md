## Problem link: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/

## Intuition:

- Making pairs in an array is a good indication for union find problems.
- Paired elements can be seen as components

## Notes:

- Once components are formed, we can find the minimum in each component according to the original order of the array.
- A slight modification of the union find algorithm can be used with the help of a map of heaps.
- for each parent we maintain a heap of elements in the component and pop the min value when asked.
- This is done while finally iterating over the original input array.