def longestZigZag(root: Optional[TreeNode]) -> int:
        maxZigLen = 0

        def dfs(node, l=0, flag=False):
            if not node: return

            nonlocal maxZigLen
            maxZigLen = max(maxZigLen, l)

            if flag:
                dfs(node.left, l + 1, False)
                dfs(node.right, 1, True)
            else:
                dfs(node.right, l + 1, True)
                dfs(node.left, 1, False)

        dfs(root)
        return maxZigLen