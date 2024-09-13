use std::f32::INFINITY;

const INF: i32 = INFINITY as i32;

pub fn run(prices: Vec<i32>) -> i32 {
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

    // in this problem -> num_transactions = 1

    let mut dp_i_0: i32 = 0;
    let mut dp_i_1: i32 = -INF;
    let mut max_pft: i32 = -INF;

    for p in prices {
        dp_i_0 = dp_i_0.max(p + dp_i_1);
        dp_i_1 = dp_i_1.max(-p + 0);

        max_pft = max_pft.max(dp_i_0);
    }
    max_pft
}