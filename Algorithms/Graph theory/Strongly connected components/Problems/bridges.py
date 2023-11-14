'''
bridges: edges in the graph that increase the number of components when removed.

Approach:
- assign a time of discovery and a low link val to each node.
- on a callback, record the minimum low link value. (represents the lowest discovery time needed to visit the entire component)
- check if the edge can be a bridge during the callback
    - if low_link[child] <= time_of_discovery[node] --> This means that edge cannot be bridge (the child can eevntually reach the node via some other node since its low_link is smaller)
    - if low_link[child] > time_of_discovery[node] --> This means that this edge can be a bridge since there is no way for child to reach node once the edge is removed.
'''

timer = 0
bridges = []

def dfs(i, p):
    visited[i] = 1
    td[i] = timer
    low[i] = timer
    timer += 1
    
    for j in adj[i]:
        if j == p: continue
        if not visited[j]:
            dfs(j, i)
            low[i] = min(low[i], low[j])
            if low[j] > td[i]: bridges.append((i, j))
        else:
            low[i] = min(low[i], low[j])