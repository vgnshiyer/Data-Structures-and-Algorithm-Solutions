'''
Approach:
- Perform DFS on any unvisited node
- Explore all its unvisited childred
- During the callback, push the node on to the stack
- Reverse the graph (take a transpose)
- pop all visited nodes from the stack
- explore all the unvisited nodes from the stack
- Store the components
'''

# O(V + E)
def dfs_1(i):
    visited[i] = True
    for j in range(n):
        if adj_mat[i][j] and not visited[j]: dfs_1(j)
    stack.append(i)

def transpose():
    for i in range(n):
        for j in range(i):
            adj_mat[i][j], adj_mat[j][i] = adj_mat[j][i], adj_mat[i][j]
            
def dfs_2(i):
    visited[i] = True
    components[i] = numComponents
    for j in range(n):
        if adj_mat[i][j] and not visited[x]: dfs(j)
       