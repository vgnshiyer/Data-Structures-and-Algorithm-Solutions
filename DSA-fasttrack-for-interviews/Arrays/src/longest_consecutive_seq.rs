use std::collections::HashSet;

// time: O(n) space: O(n)
pub fn run(nums: Vec<i32>) -> i32 {
    let num_set: HashSet<i32> = nums.iter().cloned().collect();
    let mut ans: i32 = 0;

    for n in nums {
        if num_set.contains(&(n - 1)) { continue; }
        let mut conseq_count: i32 = 0;
        let mut cur: i32 = n;

        while num_set.contains(&cur) {
            conseq_count += 1;
            cur += 1;
        }
        ans = ans.max(conseq_count);
    }
    ans
}