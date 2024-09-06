use std::{cmp, f32::INFINITY};

pub fn run(cost: Vec<i32>) -> i32 {
    let mut dp: Vec<i32> = vec![0;cost.len()+1];
    dp[cost.len()] = 0;
    for i in (0..cost.len()).rev() {
        dp[i] = cost[i];
        dp[i] += cmp::min(
            dp[i + 1],
            if i + 2 <= cost.len() {
                dp[i + 2]
            } else {
                INFINITY as i32
            }
        );
    }
    cmp::min(dp[0], dp[1])
}