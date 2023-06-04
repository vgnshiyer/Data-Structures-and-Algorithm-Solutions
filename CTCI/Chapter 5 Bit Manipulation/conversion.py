## simply XOR and count number of set bits
def conversion(a, b) -> int:
    flipCount = 0
    a ^= b
    while a:
        flipCount += 1
        a = a & (a-1) ## this operation clears the LSB
    return flipCount

if __name__ == '__main__':
    print(conversion(29, 15))