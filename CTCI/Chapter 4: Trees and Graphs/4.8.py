def lowestCommonAncestor(root, p, q):
    if root.val == p or root.val == q:
        return root

    left, right = None, None
    if root.left: left = lowestCommonAncestor(root.left, p, q)
    if root.right: right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    
    if left: return left
    if right: return right