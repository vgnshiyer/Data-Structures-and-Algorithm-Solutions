def insert(N, M, i, j) -> int:
    for ind in range(i, j + 1):
        bit = M & (1 << ind - i) != 0## extract bit from M
        N |= (bit << ind) ## set indth bit

    return N

print("N = {0:b}, M = {1:b}".format(1024, 11))
print("Ans = {0:b}".format(insert(1024, 11, 2, 6)))
    