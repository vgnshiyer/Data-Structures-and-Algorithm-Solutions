'''
Find if two trees are isomorphic
'''

from Tree import TreeNode

def isIsomorphic(g1, g2):
    c1 = treeCenter(g1) # finding_center.py
    c2 = treeCenter(g2)

    tree1 = rootTree(c1, g1) # rooting_a_graph.py

    tree1_encoded = encodeTree(tree1)

    for c in c2:
        tree2 = rootTree(c, g2)
        tree2_encoded = encodeTree(tree2)

        if tree1_encoded == tree2_encoded:
            return True
    return False

# AHU algorithm
def encodeTree(node):
    if not node: return ''

    labels = []
    for child in node.children:
        labels.append(encodeTree(child))

    labels.sort()
    return '(' + ''.join(labels) + ')'
