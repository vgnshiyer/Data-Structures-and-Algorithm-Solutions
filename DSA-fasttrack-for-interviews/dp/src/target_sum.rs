use std::collections::HashMap;

pub fn run(nums: Vec<i32>, target: i32) -> i32 {
    // state: dp[i][j] -> num ways to get sum j from pos i
    // transition: dp[i][j] = dp[i + 1][j - nums[i]] + dp[i + 1][j + nums[i]]
    // base: dp[_][target] = 1

    fn helper(i: usize, s: i32, nums: &Vec<i32>, memo: &mut HashMap<(usize, i32), i32>) -> i32 {
        if i >= nums.len() {
            return (s == 0) as i32;
        }
        if let Some(&res) = memo.get(&(i, s)) {
            return res;
        }
        let res = helper(i + 1, s - nums[i], nums, memo) + helper(i + 1, s + nums[i], nums, memo);
        memo.insert((i, s), res);
        res
    }

    let mut memo = HashMap::new();
    helper(0, target, &nums, &mut memo)
}