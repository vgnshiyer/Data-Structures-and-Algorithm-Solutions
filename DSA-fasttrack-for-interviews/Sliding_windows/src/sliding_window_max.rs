use std::collections::VecDeque;

pub fn run(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut q: VecDeque<i32> = VecDeque::new();
    let mut result: Vec<i32> = Vec::new();
    for (i, n) in nums.iter().enumerate() {
        while !q.is_empty() && *n > q[q.len() - 1] || q.len() > k as usize { q.pop_front(); }
        q.push_back(*n);
        if i >= (k - 1) as usize { result.push(q[0]); }
    }
    result
}