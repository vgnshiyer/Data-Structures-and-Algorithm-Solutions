pub fn run(amount: i32, coins: Vec<i32>) -> i32 {
    // state: dp[i][j] -> num ways to get sum j with i coins
    // transition: dp[i][j] = (without) dp[i-1][j] + (with) dp[i][j-coins[i]]
    // base: dp[_][0] = 1 (1 way to make 0 sum)

    let mut dp: Vec<Vec<i32>> = vec![vec![0;amount as usize + 1];coins.len() + 1];
    for i in 0..=coins.len() { dp[i][0] = 1; }

    for i in 1..=coins.len() {
        for j in 1..=amount as usize {
            dp[i][j] = dp[i - 1][j];
            if j as i32 - coins[i-1] >= 0 {
                dp[i][j] += dp[i][j-coins[i-1] as usize];
            }
        }
    }
    dp[coins.len()][amount as usize]
}