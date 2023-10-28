import TreeNode

def rootTree(rootId, parent=None):
    for child in neighbors[rootId]:
        if parent != None and child == parent:
            continue
            
        child = TreeNode(child.val, [])
        node.children.append(child)
        rootTree(child)
    return rootId  