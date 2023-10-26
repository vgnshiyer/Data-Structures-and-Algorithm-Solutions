def lca(A, B):
    if depth[B] < depth[A]: A, B = B, A
    
    # bring A at the same level as B
    k = depth[B] - depth[A] 
    for j in range(LOGN + 1, -1, -1):
        if k & (1 << j):
            A = up[A][j]

    if A == B: return A

    # search for nodes which is closest to the LCA
    for j in range(LOGN + 1, -1, -1):
        if up[A][j] != up[B][j]:
            A = up[A][j]
            B = up[B][j]
    
    # return immediate parent
    return up[A][0]