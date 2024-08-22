use std::collections::VecDeque;

pub fn run(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut q: VecDeque<usize> = VecDeque::new();
    let mut result: Vec<i32> = Vec::new();
    let mut l = 0;
    for r in 0..nums.len() {
        while !q.is_empty() && nums[*q.back().unwrap()] < nums[r] { q.pop_back(); }
        q.push_back(r);
        if (r - l + 1) as i32 == k {
            result.push(nums[*q.front().unwrap()]);
            l += 1;
        }
        while !q.is_empty() && *q.front().unwrap() < l { q.pop_front(); }
    }
    result
}