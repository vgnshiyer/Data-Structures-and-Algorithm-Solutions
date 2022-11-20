### Convex Hull

Convex hull is a polygon that encloses all of the points. The vertices maximize the area while minimizing the circumference.

**reference:** https://www.youtube.com/watch?v=B2AJoQSZf4M

        x
       /  \
      x x  x-----x
      |         /     <-- Here is a convex hull which covers all the 
      x     x  /          points with minimum circumference  
        \     /
         x---x

##### There are two algorithms used to compute the convex hull

**1. Graham Scan**
* Select the lowest y coordinate
* Sort them according to the angle that they make, relative to the starting point.
* iterate in sorted order, placing each point on a stack, but only if it makes counterclockwise turn relative to the previous 2 points on the stack.
* pop previous element off, if making a clockwise turn.

**2. Jarvis March**
* Select the point with the lowest y coordinate.
* loop through the other points in a brute force manner.
* Select the point with the smallest counterclockwise angle with reference to the initial point.
* repeat until reaching the starting vertex.
