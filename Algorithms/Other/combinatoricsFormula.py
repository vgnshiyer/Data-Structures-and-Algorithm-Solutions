def ncr(n, r):
    res = float(n)
    for i in range(1, r + 1):
        res *= (n - i + 1) / i
    return int(res)