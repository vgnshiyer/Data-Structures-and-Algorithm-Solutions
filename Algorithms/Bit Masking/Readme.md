### WHAT IS BIT MASKING?

Masking is a technique of deciding which bits you want to set and which bits you want to clear.

It is the act of applying a mask to a value.
There are three logical operations used normally: 

* Bitwise AND : Extract a subset of bits from the value.
* Bitwise OR : Set the a subset of the value.
* Bitwise XOR : Flip a subset of bits from the value.

Below is an example of masking a certain subset of a binary number.

value : 01010101b
mask :  00001111b &
____________________
        00000101b
mask first four bits and extract the rest.

##### In the example subsequences.cpp, you will find the application of using bitmasking to a common problem of finding the number of subsequences of a given string.

Normally this problem is solved using recursion and backtracking which will go through all possible subsets by mainly making two choices at every step. (to include the current character or to exclude it).

Let's see the application of bit masking to this problem.

Given a string ABC, possible subsequences are [_, A, B, C, AB, AC, BC, ABC]
as we can see, given a string of length 'n', there can be total 2^n-1 subsequences.

Therefore we can have a mask of length 3 which loops from 0 to 2^n-1.
In this case, it would loop from 0 to 7(inclusive).
For every bit that is set, we include the corresponding character, and ignore the characters for which the corresponding bits are unset.

eg. 
        ABC
        000 = _
        001 = C
        010 = B
    &   011 = BC
        100 = A
        101 = AC
        110 = AB
        111 = ABC

Checkout the cpp file for the program in detail.
