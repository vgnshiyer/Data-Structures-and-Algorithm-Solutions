@cache
def getSum(self, root):
    if not root: return 0
    return root.val + self.getSum(root.left) + self.getSum(root.right)

def maxProduct(self, root: Optional[TreeNode]) -> int:
    def dfs(root, sumSoFar=0):
        if not root: return 0

        leftSum = self.getSum(root.left)
        rightSum = self.getSum(root.right)

        sumSoFar += root.val

        leftMax = dfs(root.left, sumSoFar + rightSum)
        rightMax = dfs(root.right, sumSoFar + leftSum)

        splitleft = leftSum * (sumSoFar + rightSum)
        splitright = rightSum * (sumSoFar + leftSum)

        return max([leftMax, rightMax, splitleft, splitright])
    return dfs(root) % (10 ** 9 + 7)