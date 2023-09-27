def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    sorted_by_age = sorted(zip(ages, scores), key = lambda x: (x[0], x[1]))
    n = len(sorted_by_age)
    dp = [0] * n

    dp[0] = sorted_by_age[0][1]
    maxScore = dp[0]
    for i in range(1, n):
        age, score = sorted_by_age[i]
        dp[i] = score
        for j in range(i):
            prev_player_age, prev_player_score = sorted_by_age[j]
            if age == prev_player_age or (age > prev_player_age and score >= prev_player_score):
                dp[i] = max(dp[i], score + dp[j])
        maxScore = max(maxScore, dp[i])

    return maxScore