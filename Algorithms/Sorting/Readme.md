## Sorting Algorithms
Sorting is a technique that is implemented to arrange the data in a specific order. Sorting is required to ensure that the data which we use is in a particular order so that we can easily retrieve the required piece of information from the pile of data.

### Bubble Sort
For every position from 0 to n-1, bubble sort performs n comparisons to find the smallest element possible at the current position. As soon as it finds an element smaller than the element at current position, it performs a swap. Therefore, in the below example, bubble sort will place 5 as the first position in the first pass. For bring 5 there, it makes 3 comparisons. Below is a complete output for the below example.

eg: 
arr = {12, 45, 8, 5, 16}

Array before sorting..12 45 8 5 16 

Bubble sort visualization : 
12 45 8 5 16 
swapping 0 and 2
8 45 12 5 16 
swapping 0 and 3
5 45 12 8 16 
finished pass : 0

5 45 12 8 16 
swapping 1 and 2
5 12 45 8 16 
swapping 1 and 3
5 8 45 12 16 
finished pass : 1

5 8 45 12 16 
swapping 2 and 3
5 8 12 45 16 
finished pass : 2

5 8 12 45 16 
swapping 3 and 4
5 8 12 16 45 
finished pass : 3

5 8 12 16 45 
finished pass : 4

Array after sorting..
5 8 12 16 45 

**Time Complexity:**
Best: O(n) -> using a flag variable
Avg: O(n^2)
Worst: O(n^2)

**Space Complexity:**
O(1)

### Selection Sort
Selection sort is a bit different from Bubble sort, in a way that it skips directly to the element which is the smallest in the rest of the array and places it in its desired position.

eg:
Array before sorting..
12 45 8 15 33 

Selection sort visualization : 
12 45 8 15 33 
swapping 0 and 2
8 45 12 15 33 
placed 0th element 

8 45 12 15 33 
swapping 1 and 2
8 12 45 15 33 
placed 1th element 

8 12 45 15 33 
swapping 2 and 3
8 12 15 45 33 
placed 2th element 

8 12 15 45 33 
swapping 3 and 4
8 12 15 33 45 
placed 3th element 

8 12 15 33 45 
swapping 4 and 4
8 12 15 33 45 
placed 4th element 

Array after sorting..
8 12 15 33 45 

**Time Complexity:**
Best: O(n^2)
Avg: O(n^2)
Worst: O(n^2)

**Space Complexity:**
O(1)

### Insertion Sort
Insertion sort gets the current element and compares it to its predecessors, skips all the elements greater than and equal to it, and places it in its appropriate position.

eg.
Array before sorting..
12 45 8 15 33 

Insertion sort visualization : 
12 45 8 15 33 
Placing cur to its position
12 45 8 15 33 
12 45 8 15 33 
Placing cur to its position
12 45 8 15 33 
12 45 8 15 33 
Placing cur to its position
8 12 45 15 33 
8 12 45 15 33 
Placing cur to its position
8 12 15 45 33 
8 12 15 45 33 
Placing cur to its position
8 12 15 33 45 
Array after sorting..
8 12 15 33 45

**Time Complexity:**
Best: O(n)
Avg: O(n^2)
Worst: O(n^2)

**Space Complexity:**
O(1)

### Quick Sort
Quick sort is the most efficient algorithm that can be used to sort the data. This technique uses the “divide and conquer” strategy in which the problem is divided into several subproblems and after solving these subproblems individually are merged together for a complete sorted list.

In quicksort, we first divide the list around the pivot element and then place the other elements in their proper positions according to the pivot element.

eg.
Array before sorting..
[12, 45, 8, 5, 16]

Quick Sort Visualization:

Partition for range 0-4:
[12, 8, 5, 16, 45]
pivot at idx : 3
Partition for range 0-2:
[5, 8, 12, 16, 45]
pivot at idx : 0
Partition for range 1-2:
[5, 8, 12, 16, 45]
pivot at idx : 2

Array after sorting..
[5, 8, 12, 16, 45]

**Time Complexity:**
Best: O(nlogn)
Avg: O(nlogn)
Worst: O(nlogn)

**Space Complexity:**
O(n)

### Merge Sort
This is another technique that uses the “Divide and conquer” strategy. In this technique, we divide the list first into equal halves. Then we perform merge sort technique on these lists independently so that both the lists are sorted. Finally, we merge both the lists to get a complete sorted list.

Merge sort and quick sort are faster than most other sorting techniques. Their performance remains intact even when the list grows bigger in size.

eg.
Array before sorting..
12 45 8 5 16 

Merge Sort Visualization : 
Current Range : 0 0 1
Conquered : 
12 45 
Current Range : 0 1 2
Conquered : 
8 12 45 
Current Range : 3 3 4
Conquered : 
5 16 
Current Range : 0 2 4
Conquered : 
5 8 12 16 45 

Array after sorting..
5 8 12 16 45

**Time Complexity:**
Best: O(nlogn)
Avg: O(nlogn)
Worst: O(nlogn)

**Space Complexity:**
O(n)