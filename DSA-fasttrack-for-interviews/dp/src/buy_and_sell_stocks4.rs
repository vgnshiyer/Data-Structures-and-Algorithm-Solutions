pub fn run(num_trans: i32, prices: Vec<i32>) -> i32 {
    // state: 
        // dp[i][j][0] -> cost, with no stock in hand, with j transactions left
        // dp[i][j][1] -> cost, with 1 stock in hand, with j transactions left
    // transition: 
        // dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])  -> we get money when we sell
        // dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])  -> there is a cost of keeping a stock in hand (price of the stock)
    // base:
        // dp[0][_][0] = 0 -> cost of holding no stock at 0th day
        // dp[0][_][1] = -inf -> cost of holding 1 stock on 0th day (impossible)
        // dp[_][0][0] = 0 -> cost of holding 0 stocks with no transactions left
        // dp[_][0][1] = -inf -> cost of holding 1 stock with no transactions left

    let n: usize = prices.len();
    let mut dp: Vec<Vec<Vec<i32>>> = vec![vec![vec![0; 2]; num_trans as usize + 1]; n + 1];
    const INF: i32 = i32::MAX;

    for j in 0..=num_trans as usize {
        dp[0][j][0] = 0;
        dp[0][j][1] = -INF;
    }

    for i in 0..=n {
        dp[i][0][0] = 0;
        dp[i][0][1] = -INF;
    }

    for i in 1..=n {
        for j in 1..=num_trans as usize {
            dp[i][j][0] = dp[i - 1][j][0].max(prices[i - 1] + dp[i - 1][j][1]);
            dp[i][j][1] = dp[i - 1][j][1].max(-prices[i - 1] + dp[i - 1][j - 1][0])
        }
    }
    dp[n][num_trans as usize][0]
}