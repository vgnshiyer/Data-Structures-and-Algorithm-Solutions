use std::collections::HashMap;

pub fn run(nums: Vec<i32>) -> bool {
    // state: dp[i] -> partition with sum i possible?
    // transition: dp[i] + n for all i for all n if dp[i]
    // base: dp[0] = true
    let mut total: i32 = nums.iter().sum();
    if total & 1 != 0 { return false; }
    total >>= 1;

    let mut dp: HashMap<i32, bool> = HashMap::new();
    dp.insert(0, true);  // partition with sum 0 is possible

    for n in nums {
        let mut new_dp = dp.clone();
        for (&k, &v) in dp.iter() {
            if v {
                new_dp.insert(k + n, true);
            }
        }
        dp = new_dp;
    }
    dp.get(&total).copied().unwrap_or(false)
}