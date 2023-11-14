'''
Articulation point: points in the graph that increase the number of components when removed.
'''

articulation = []
idx = 0

def dfs(i, p):
    visited.add(i)

    td[i] = idx
    low[i] = idx
    for j in adj[i]:
        if j == p: continue
        if j not in visited:
            dfs(j, i)
            low[i] = min(low[i], low[j])
            if low[j] >= td[i] and p != -1: articulation.append(i) # can reach its parent
        else:
            low[i] = min(low[i], td[j]) 