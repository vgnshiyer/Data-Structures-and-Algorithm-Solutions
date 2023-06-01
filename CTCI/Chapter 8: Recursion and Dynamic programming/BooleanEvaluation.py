def countEval(booleanString, result, memo) -> int:
    if len(booleanString) == 0: return 0
    if len(booleanString) == 1: return result

    if booleanString + str(result) in memo: return memo[booleanString + str(result)]

    nways = 0
    for i in range(1, len(booleanString), 2):
        operator = booleanString[i]
        left = booleanString[:i]
        right = booleanString[i+1:]

        leftTrue = countEval(left, True, memo)
        leftFalse = countEval(left, False, memo)
        rightTrue = countEval(right, True, memo)
        rightFalse = countEval(right, False, memo)

        if operator == '^':
            if result == True:
                ans = (leftTrue * rightFalse) +  (leftFalse * rightTrue)
            else:
                ans = (leftTrue * rightTrue) + (leftFalse * rightFalse)
        elif operator == '|':
            if result == True:
                ans = (leftTrue * rightFalse) + (leftFalse * rightTrue) + (leftTrue * rightTrue)
            else:
                ans = (leftFalse * rightFalse)
        elif operator == '&':
            if result == True:
                ans = (leftTrue * rightTrue)
            else:
                ans = (leftTrue * rightFalse) + (leftFalse * rightTrue) + (leftFalse * rightFalse)
        nways += ans

    memo[booleanString + str(result)] = nways
    return nways

if __name__ == '__main__':
    booleanString = '0&0&0&1^1|0'
    result = True

    memo = {}
    print(countEval(booleanString, result, memo))