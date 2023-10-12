def rob(root: Optional[TreeNode]) -> int:
    @cache
    def getMaxProfit(node, f=False):
        if not node: return 0

        r = node.val + getMaxProfit(node.left, True) + getMaxProfit(node.right, True) if not f else -float('inf')
        n_r = getMaxProfit(node.left) + getMaxProfit(node.right)
        return max(n_r, r)

    return getMaxProfit(root)