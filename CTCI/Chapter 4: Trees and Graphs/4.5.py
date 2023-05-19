## https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    LEFTMAX = -2**31 - 1
    RIGHTMAX = 2**31
    
    def validate(self, root, leftBoundary, rightBoundary):
        if not root:
            return True
        if root.val <= leftBoundary or root.val >= rightBoundary:
            return False
        
        isLeftValid = self.validate(root.left, leftBoundary, root.val)
        isRightValid = self.validate(root.right, root.val, rightBoundary)
        return isLeftValid & isRightValid
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, self.LEFTMAX, self.RIGHTMAX)