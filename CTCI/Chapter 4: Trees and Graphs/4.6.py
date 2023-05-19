def inOrderSuccessor(node):
    if not node:
        return node

    if(node.right): ## node has right child
        return leftMostOfRightChild(node.right)
    else:
        if node.parent.left is node:
            return node.parent
        else:
            return inOrderSuccessor(node.parent)

def leftMostOfRightChild(node):
    if not node: return node

    if not node.left: return node

    return leftMostOfRightChild(node.left)