use std::{cmp, f32::INFINITY};

const inf: i32 = INFINITY as i32;

pub fn run(nums: Vec<i32>) -> i32 {
    let n = nums.len();
    let mut dp: Vec<i32> = vec![inf;n];
    dp[n - 1] = 0;

    for i in (0..nums.len()-1).rev() {
        let end = cmp::min(n-1, i + nums[i] as usize);
        for j in i+1..=end {
            if dp[j] != inf {
                dp[i] = cmp::min(dp[i], 1 + dp[j])
            }
        }
    }
    dp[0]
}