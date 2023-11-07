### Properties of edges in a graph

Tree edges: These are edges in the DFS traversal that lead to a node that hasn't been visited yet.
Back edges: These are edges that point back to an ancestor in the DFS traversal.
Forward edges: These are non-tree edges that point to a descendant in the DFS traversal.
Cross edges: These are all other edges. They can go between vertices in the same level or jump levels, but they don't point back to an ancestor.