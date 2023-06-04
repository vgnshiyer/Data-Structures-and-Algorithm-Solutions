'''
    To get a number larger than n with same set bits,
    11011001111100  ==> 11011010001111
          |        ~ find the rightmost 0 bit with ones to its right
                   ~ flip it
                   ~ move ones after that bit to as right as possible to minimize the magnitude of the number

    To get a number smaller than n with same set bits,
    11011001111100  ==> 11011001111010
               |   ~ find the rightmost 1 bit with zeros to its right
                   ~ flip it
                   ~ move all ones after that bit to as closest to its right as possible
'''
def getNext(num) -> int:
    zerosToRight, onesToRight = 0, 0
    temp = num

    while(temp and temp & 1 == 0):
        zerosToRight += 1
        temp >>= 1

    while(temp and temp & 1 == 1):
        onesToRight += 1
        temp >>= 1

    firstNonTralingZero = zerosToRight + onesToRight

    num |= (1 << firstNonTralingZero) ## flipping first zero bit
    num &= ~((1 << firstNonTralingZero) - 1) ## clear bits to the right of the bit
    num |= (1 << (onesToRight-1)) - 1 ## shifting ones to the right as much as possible
    return num

def getPrev(num) -> int:
    zerosToRight, onesToRight = 0, 0
    temp = num

    # notice the difference between getNext
    while(temp and temp & 1 == 1):
        onesToRight += 1
        temp >>= 1

    while(temp and temp & 1 == 0):
        zerosToRight += 1
        temp >>= 1

    firstNonTralingOne = zerosToRight + onesToRight
    num &= (~0 << (firstNonTralingOne + 1)) ## clearing p + 1 bits
    num |= ((1 << onesToRight + 1) - 1) << zerosToRight-1
    return num

def printBinary(num):
    print('{0:b}'.format(num))

if __name__ == '__main__':
    printBinary(13948) # 11011001111100
    printBinary(getNext(13948)) # 11011010001111
    printBinary(getPrev(13948)) # 11011001111010