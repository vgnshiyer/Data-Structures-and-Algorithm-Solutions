## Construct binary search tree from sorted array

class Node:
    left = None
    right = None
    data = -1

    def __init__(self, data):
        self.data = data

def constructBST(nodes):
    if nodes == []:
        return None

    length = len(nodes)
    mid = length // 2

    root = Node(nodes[mid])
    root.left = constructBST(nodes[:mid])
    root.right = constructBST(nodes[mid+1:])
    return root

def inorder(node):
    if not node:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)

if __name__ == '__main__':
    root = constructBST([1,2,3,4,5,6,7])

    inorder(root)