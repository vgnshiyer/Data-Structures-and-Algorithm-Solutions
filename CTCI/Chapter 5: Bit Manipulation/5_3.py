## you can flip exactly one bit -> find the longest contiguous sequence of 1s you can make

## using dp : O(b) time O(b) space
def flipToWin(num):
    n = len(num)
    dp = [0] * n

    counter = 0
    for i, c in enumerate(num):
        if c == '0':
            dp[i] = counter
            counter = 0
        else:
            counter += 1

    ans = 1
    counter = 0
    for i in range(n-1, -1, -1):
        c = num[i]
        if c == '0':
            ans = max(ans, dp[i] + counter + 1)
            counter = 0
        else:
            counter += 1
    return ans

## cooler way : O(b) time O(1)
def flipToWin2(num):
    if ~num == 0: return num.bit_length()

    bestLength = 1 ## can always be 1
    previousLength = 0
    currentLength = 0
    while(num > 0):
        if num & 1:
            currentLength += 1
        else:
            previousLength = 0 if (num & 2) == 0 else currentLength ## 101
            currentLength = 0
        bestLength = max(bestLength, currentLength + previousLength + 1)
        num >>= 1
    return bestLength

if __name__ == '__main__':
    ## for simplicity passing the binary string instead
    print(flipToWin('1101111101010001111')) # 8

    print(flipToWin2(457359)) # 8