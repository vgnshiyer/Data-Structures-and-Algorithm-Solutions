## Bit Manipulation

All data in a computer is represented as 0's and 1's.
The Binary representation of a number 22 is
2 + 4 + 16 = (10110)2

**1*2^4 + 0*2^3 + 1*2^2 + 1*2^1 + 0*2^0**

The bit representation can be signed or unsigned. In c++ the a signed integer type variable value ranges from -2^31 to 2^31 - 1. The first bit of the number represents whether the number is positive or negative.
Two's complement is used, which means inverting all the bits of a number and adding a 1 to the Least Significant Bit(LSB).

If a number is larger than the upper bound of a data type, then the number will overflow. 
For eg.
```
int x = 2147483647
cout << x << endl; // 2147483647
x++;
cout << x << endl; // -2147483648
```

#### Bitwise Operations

**AND Operation** : both bits 1 => 1

  0101 (5)
& 1001 (9)
= 0001 (1)

Using the AND operation, we can find whether a number is even or odd using x&1 == 1 (if odd).

**OR Operation** : both bits 0 => 0

  0101 (5)
& 1001 (9)
= 1101 (13)

**NOT Operation**

~29 = -30 (1's complement)

**XOR Operation** : both bits different => 1

  0101 (5)
& 1001 (9)
= 1100 (11)

**Bit Shift**

A left bit shift x << k appends k zeros to the right of the number.
A left shift mutltiplies 2^k to the number.
A right bit shift x >> k removes k bits from the lsb.
A right shift divides 2^k from the number.