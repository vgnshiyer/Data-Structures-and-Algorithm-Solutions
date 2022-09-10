### USACO
##### Section 2.4 Solutions

**Problem 1.** The Tamworth Two

**Approach:**
We simulate both the cow and the farmer from their particular starting positions. 
Simultaneously, we also count the current time.
Once both the cow and the farmer meet, we simple print the current time.

If a state is revisited in the course, we discover that it is Impossible for the cow and the farmer to meet. Hence, in such a case we print 0;


**Problem 2.** Overfencing

**Approach:**
/* FLOOD FILL Algorithm*/
Basically, we do a Depth First Search to every cell that is reachable from each exit.
Once we find a shorter path to either of the exit from a particular cell, we simply replace the shorter path in the distance array.

**Notice** that we do not have any visited boolean array to maintain cells that were visited previously. This is because here we not only care about if a cell is reachable or not, but also about the shortest path to the cell. Therefore, we always look for shorter paths reaching the particular cell.


**Problem 4.** Bessie Come Home

**Approach:**
This is a classic example of finding the shortest path between two nodes in a weighted undirected graph.
This can be done simply using the Dijkstra's Algorithm. (The cow nearest to the milking house will reach first).


**Problem 5.** Fractions to Decimal

**Approach:**
At every step, we take the modulo of the numerator and multiple it by 10. 
We store the quotients in a map.
We store all the numerators in a hashmap(unordered set), and if we come across the same numerator in our operations, we discover a recurrence in the decimals. 
Hence we stop our algorithm and print the reqd output.