use std::cmp;

pub fn run(nums: Vec<i32>) -> i32 {
    if nums.len() == 1 { return nums[0]; }
    // state: dp[i] -> max money robbed till this house
    // transition: dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    // base case: dp[0] = nums[0] dp[1] = max(nums[1], nums[0])
    let mut dp: Vec<i32> = vec![0;nums.len()];
    dp[0] = nums[0];
    dp[1] = cmp::max(nums[0], nums[1]);
    for i in 2..nums.len() {
        dp[i] = cmp::max(
            dp[i - 1],
            nums[i] + dp[i - 2]
        )
    }
    dp[nums.len() - 1]
}