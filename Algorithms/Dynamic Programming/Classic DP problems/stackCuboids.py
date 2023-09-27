def maxHeight(cuboids: List[List[int]]) -> int:
    '''
    We can orient the cuboids in the way we want. Therefore, we sort the cuboid dimensions in ascending order, keeping the height at the end.
    Next we sort all the cuboids by the smallest dimension as while comparing any two cuboids, the smallest dimension must be smaller or equal to the other cuboid's smallest dimension.

    1. sort the individual cuboids so that we get the maximum height.
    2. sort the cuboids by l*b, so the cuboid with minimum b*l will be at the top.
    '''

    for cub in cuboids: cub.sort()
    cuboids.sort()
    dp = [x[2] for x in cuboids]

    maxHeight = dp[0]
    for i in range(1, len(cuboids)):
        for j in range(i):
            if cuboids[i][0] >= cuboids[j][0] and cuboids[i][1] >= cuboids[j][1] and cuboids[i][2] >= cuboids[j][2]: dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        maxHeight = max(maxHeight, dp[i])
    
    return maxHeight