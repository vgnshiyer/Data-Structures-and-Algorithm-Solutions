def minSwapsCouples(row: List[int]) -> int:
    '''
    It is similar to finding the number of swaps to make permutation resolved.
    n - 1

    eg. 2 3 1 0
    swaps: 3--0, 0--2, 1--2
    This is just like adding edges to make them as one component. 

    In this problem tho, we need to consider pairs of indices instead of individual indices.
    (0, 1), (2, 3), (4, 5) and so on...

    '''

    n = len(row)
    parent = [i for i in range(n // 2)]
    edge_count = 0

    def find(a):
        if a != parent[a]:
            a = find(parent[a])
        return a
    
    def union(a, b):
        if find(a) == find(b): return
        parent[find(b)] = find(a)
        nonlocal edge_count
        edge_count += 1

    for i in range(n // 2):
        a = row[2 * i]
        b = row[2 * i + 1]
        union(a // 2, b // 2)
        '''
        If they are a couple, we will get the same component, therefore we will not add an edge. 
        eg. 0 // 2 == 1 // 2

        If they are different components, we need add en edge (swap 2 vals between these components and make them one)
        '''
    return edge_count