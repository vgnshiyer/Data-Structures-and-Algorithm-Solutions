'''
Repeated sub problems: Checking BST and Finding subtree sum
'''
@cache
def validBst(self, root, l=-float('inf'), r=float('inf')):
    if not root: return True
    if root.val <= l or root.val >= r: return False
    return self.validBst(root.left, l, root.val) and self.validBst(root.right, root.val, r)

@cache
def getSum(self, root):
    if not root: return 0
    return root.val + self.getSum(root.left) + self.getSum(root.right)

def maxSumBST(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    
    left = self.maxSumBST(root.left)
    right = self.maxSumBST(root.right)
    cur = (root.val + self.getSum(root.left) + self.getSum(root.right)) if self.validBst(root) else -float('inf')
    return max([0, cur, left, right])