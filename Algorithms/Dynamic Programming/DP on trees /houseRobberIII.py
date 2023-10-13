def rob(root: Optional[TreeNode]) -> int:
    @cache
    def getMaxProfit(node, f=False):
        if not node: return 0

        r = node.val + getMaxProfit(node.left, True) + getMaxProfit(node.right, True) if not f else -float('inf')
        n_r = getMaxProfit(node.left) + getMaxProfit(node.right)
        return max(n_r, r)

    return getMaxProfit(root)

def rob_spaceOptimized(root: Optional[TreeNode]) -> int:
    @cache
    def getMaxProfit(node):
        if not node: return (0, 0)

        left, right = getMaxProfit(node.left), getMaxProfit(node.right)
        return (max(node.val + left[1] + right[1], left[0] + right[0]), left[0] + right[0])

    return getMaxProfit(root)[0]