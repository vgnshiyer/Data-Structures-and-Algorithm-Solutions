def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if preorder == [] or inorder == []:
        return None
    
    root = TreeNode(preorder[0])
    pos = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
    root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
    return root