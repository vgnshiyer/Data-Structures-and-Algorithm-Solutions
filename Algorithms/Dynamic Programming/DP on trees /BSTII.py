def generateTrees(n: int) -> List[Optional[TreeNode]]:
    @cache
    def makeBsts(l, r):
        if l > r: return [None]

        trees = []
        for i in range(l, r + 1):
            l_trees, r_trees = makeBsts(l, i - 1), makeBsts(i + 1, r)

            for j in range(len(l_trees)):
                for k in range(len(r_trees)):
                    trees.append(TreeNode(i, l_trees[j], r_trees[k]))
        return trees

    return makeBsts(1, n)