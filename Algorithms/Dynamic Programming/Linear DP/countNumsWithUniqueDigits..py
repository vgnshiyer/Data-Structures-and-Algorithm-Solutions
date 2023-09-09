def countNumbersWithUniqueDigits(n: int) -> int:
    '''
    n = 1, ans = 10 (0...10)
    n = 2, _ _, first digit can have 9 possible values (1..9), second digit can have 9 possible values (0..10) excluding the one selected in first digit.
    therefore for n = 2, ans = 10 + 81 (10 for one digit numbers )
    '''

    if n == 0: return 1

    ans, b = 10, 9

    for i in range(2, n+1):
        b *= (9 - i + 2)
        ans += b
    
    return ans