use std::{cmp, f32::INFINITY};

pub fn run(nums: Vec<i32>) -> i32 {
    // state: dp[i] -> max sum ending at i
    // transition: dp[i] = max(dp[i - 1] + arr[i], arr[i])
    // base case: dp[0] = arr[0]

    let mut dp: Vec<i32> = vec![0;nums.len()];
    dp[0] = nums[0];
    let mut max_sum: i32 = dp[0];

    for i in 1..nums.len() {
        dp[i] = cmp::max(dp[i - 1] + nums[i], nums[i]);
        max_sum = max_sum.max(dp[i]);
    }
    max_sum
}