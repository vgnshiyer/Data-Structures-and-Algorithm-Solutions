'''
Approach:
- Maintain a stack, a being_visited array
- Maintain ids and low_link arrays
- While doing a dfs, assign a unique id to each node
- Mark it as being visited
- While exploring its children if they are unvisited dfs into them
- During the callback if the child is in the current cycle (being_visited), update current node's low_link with the minimum of itself and the child's low_link val
- Finally, pop all nodes from the stack until stack.top = node (start of scc)
'''

# O(V + E) Time
def dfs(i):
    stack.append(i)
    being_visited[i] = True
    ids[i] = idx
    low[i] = idx
    idx += 1
    
    for j in adj[i]:
        if ids[j] == -1: dfs(j)
        if being_visited[j]: low[i] = min(low[i], low[j]) # in a cycle
        
    if ids[i] == low[i]: found the start of an scc
        node = None
        while node != i:
            node = stack.pop()
            being_visited[node] = False
            low[node] = ids[i]
    scc_count += 1
 