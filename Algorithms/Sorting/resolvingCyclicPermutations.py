def resolve(perm):
    nswaps = 0

    for i in range(len(perm)):
        j = perm[i]
        while i != j:
            perm[i], perm[j] = perm[j], perm[i]
            j = perm[i]
            nswaps += 1
    return nswaps # n - 1

if __name__ == '__main__':
    perm = [2, 3, 1, 0]
    print(resolve(perm))