def countEval(booleanString, result) -> int:
    if len(booleanString) == 0: return 0
    if len(booleanString) == 1: return result

    nways = 0
    for i in range(1, len(booleanString), 2):
        operator = booleanString[i]
        left = booleanString[:i]
        right = booleanString[i+1:]

        leftTrue = countEval(left, True)
        leftFalse = countEval(left, False)
        rightTrue = countEval(right, True)
        rightFalse = countEval(right, False)

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
    return nways

if __name__ == '__main__':
    booleanString = '0&0&0&1^1|0'
    result = False

    print(countEval(booleanString, result))