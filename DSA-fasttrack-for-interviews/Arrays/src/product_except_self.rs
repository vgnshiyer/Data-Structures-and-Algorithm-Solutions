// time: O(n) space: O(n)
pub fn run(nums: Vec<i32>) -> Vec<i32> {
    let mut pre: Vec<i32> = nums.clone();
    let mut suf: Vec<i32> = nums.clone();
    for i in 0..nums.len() {
        if i > 0 {
            pre[i] *= pre[i - 1];
        }
    }
    for i in (0..nums.len()).rev() {
        if i < nums.len() - 1 {
            suf[i] *= suf[i + 1];
        }
    }

    let mut result = Vec::new();
    for i in 0..nums.len() {
       let prev = if i > 0 { pre[i - 1] } else { 1 };
       let next = if i < nums.len() - 1 { suf[i + 1] } else { 1 };
       result.push(prev * next);
    }
    result
}