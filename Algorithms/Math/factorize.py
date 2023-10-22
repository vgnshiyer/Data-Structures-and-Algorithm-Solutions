## generate factors for numbers n + 1

import random

n = random.randInt(100)
factors = [[] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(2 * i, n + 1, i):
        factors[j].append(i)