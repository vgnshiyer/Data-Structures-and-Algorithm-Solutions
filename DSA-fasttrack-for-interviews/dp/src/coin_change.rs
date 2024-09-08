use std::f32::INFINITY;

const inf: i32 = INFINITY as i32;

pub fn run(coins: Vec<i32>, amount: i32) -> i32 {
    // state: dp[i] -> min coins to get sum i
    // transition: dp[i] = min(1 + dp[i-coins[j]]) for j in 0..coins.len()
    // base case: dp[0] = 0 (0 coins needed for sum of 0)

    let n: usize = amount as usize;
    let mut dp: Vec<i32> = vec![inf;n+1];
    dp[0] = 0;

    for i in 1..=n {
        for j in 0..coins.len() {
            let c: usize = coins[j] as usize;
            if i >= c {
                if dp[i - c] == inf { continue; }
                dp[i] = dp[i].min(1 + dp[i - c]);
            }
        }
    }
    if dp[n] == inf { -1 } else { dp[n] }
}