def stoneGameII(self, nums: List[int]) -> int:
    @cache
    def minimax(i, M, maxplayer=False):
        if i >= len(nums): return 0

        if maxplayer:
            return max([
                sum(nums[i:i+x]) + minimax(i+x, max(M,x), False)
                for x in range(1, 2 * M + 1)
            ], default = -inf)
        else:
            return min([
                minimax(i+x, max(M, x), True)
                for x in range(1, 2 * M + 1)
            ], default = inf)

    return minimax(0, 1, True)