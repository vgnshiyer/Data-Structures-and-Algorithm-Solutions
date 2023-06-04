## check subtree

'''
couple other solutions:
1. create traversal strings for both and check if T2 is a substring of T1
'''

class solution:
    def isIdentical(self, tree1, tree2) -> bool:
        if not tree1 and not tree2:
            return True
        
        if not tree1: return False
        if not tree2: return False
        
        if tree1.val != tree2.val:
            return False
        
        return self.isIdentical(tree1.left, tree2.left) and self.isIdentical(tree1.right, tree2.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.isIdentical(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)