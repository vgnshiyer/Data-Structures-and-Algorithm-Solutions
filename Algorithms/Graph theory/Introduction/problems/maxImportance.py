def maximumImportance(n: int, roads: List[List[int]]) -> int:
    degree = [0] * n
    for i, j in roads:
        degree[i] += 1
        degree[j] += 1

    cities = sorted(range(n), key = lambda x: degree[x])

    val = [0] * n
    for i, c in enumerate(cities):
        val[c] = i + 1
        
    return sum(
        [val[i] + val[j] for i, j in roads]
    )