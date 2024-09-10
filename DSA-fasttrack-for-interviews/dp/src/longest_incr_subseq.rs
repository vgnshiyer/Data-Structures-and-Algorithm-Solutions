pub fn run(nums: Vec<i32>) -> i32 {
    // state: dp[i] -> longest increasing subsequence ending at i
    // transition: dp[i] = max(dp[i], 1 + dp[j]) if nums[i] > nums[j] for j in 0..i
    // base: dp[i] = 1

    let mut dp: Vec<i32> = vec![1;nums.len()];
    let mut max_len: i32 = 1;
    for i in 1..nums.len() {
        for j in 0..i {
            if nums[j] < nums[i] {
                dp[i] = dp[i].max(1 + dp[j]);
            }
        }
        max_len = max_len.max(dp[i]);
    }
    max_len
}