def wiggleMaxLength(self, nums: List[int]) -> int:
    '''
    we either include current element or ignore it from our sequence
    we take the max output from either of the decisions

    state: dp[i][x][0] -> longest wiggle sequence at i, current diff is positive
            dp[i][x][1] -> longest wiggle sequence at i, prev element x, current diff should be negative
    '''

    dp = {}
    def go(i, x, f):
        if i >= len(nums):
            return 0

        if (i, x, f) not in dp:
            # include current element
            include = 0
            if (f and nums[i] - x < 0) or (not f and nums[i] - x > 0):
                include = 1 + go(i+1, nums[i], f ^ 1)

            # exclude current element
            exclude = go(i+1, x, f)

            dp[(i, x, f)] = max(exclude, include)
        return dp[(i, x, f)]

    return 1 + max(go(1, nums[0], 0), go(1, nums[0], 1))

def wiggleMaxLength_iterative(nums: list[int]) -> int:
    '''
    we either include current element or ignore it from our sequence
    we take the max output from either of the decisions

    state: dp[i][x][0] -> longest wiggle sequence at i, current diff is positive
            dp[i][x][1] -> longest wiggle sequence at i, prev element x, current diff should be negative

    transition: dp[i][x][0] = 1 + dp[i+1][nums[i]][1] if x - nums[i] > 0
                dp[i][x][1] = dp[i+1][x][0]
    '''
    m = max(nums) + 1
    dp = [[[0]*2 for _ in range(m)] for _ in range(len(nums) + 1)]
    ans = 1
    for i in range(len(nums)-1, -1, -1):
        for j in range(m):
            if (j - nums[i] > 0): dp[i][j][0] = 1 + dp[i+1][nums[i]][1]
            if (j - nums[i] < 0): dp[i][j][1] = 1 + dp[i+1][nums[i]][0]

            dp[i][j][0] = max(dp[i][j][0], dp[i+1][j][0])
            dp[i][j][1] = max(dp[i][j][1], dp[i+1][j][1])
            ans = max([ans, dp[i][j][0], dp[i][j][1]])

    return ans

def wiggleMaxLength_iterative_space_optimized(nums: list[int]) -> int:
    '''
    state: up[i] -> longest wiggle sequence pointing upwards
            down[i] -> longest wiggle sequence pointing downwards

    transition: if nums[i] > nums[i-1]: up[i] = down[i-1] + 1; down[i] = down[i-1]
                if nums[i] < nums[i-1]: down[i] = up[i-1] + 1; up[i] = up[i-1]

    base case: up[0] = down[0] = 1
    '''

    up = down = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            '''
            Proof: We consider a subsequence of type D in {0,...,i-1} (its length is down[i-1]).
                Let N be the last number of this subsequence.
                - If nums[i] > N, then we can add nums[i] to the subsequence and it gives us a longer
                valid subsequence of type U.
                - If nums[i] <= N, then:
                (1) N cannot be nums[i-1], because nums[i-1] < nums[i] <= N i.e. nums[i-1] < N
                (2) We can replace N with nums[i-1] (we still have a valid
                subsequence of type D since N >= nums[i] > nums[i-1] i.e. N > nums[i-1]),
                and then add nums[i] to the subsequence, and we have a longer subsequence of type U.
                Therefore up[i] = down[i-1] + 1
                
                There is no gain in using nums[i] to make a longer subsequence of type D.
                Proof: Let N be the last number of a subsequence of type U
                in {0,...,i-1}.
                Assume we can use nums[i] to make a longer subsequence of type D. Then:
                (1) N cannot be nums[i-1], otherwise we would not be able to use nums[i]
                to make a longer subsequence of type D as nums[i] > nums[i-1]
                (2) Necessarily nums[i] < N, and therefore nums[i-1] < N since nums[i-1] < nums[i].
                But this means that we could have used nums[i-1] already to make a longer
                subsequence of type D.
                So even if we can use nums[i], there is no gain in using it, so we keep the old value of
                down (down[i] = down[i-1])
            '''
            up = down + 1
        elif nums[i] < nums[i-1]:
            down = up + 1

    return max(up, down)