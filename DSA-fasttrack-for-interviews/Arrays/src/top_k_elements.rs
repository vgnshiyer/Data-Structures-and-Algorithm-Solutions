use std::collections::HashMap;

pub fn run(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut count: HashMap<i32, i32> = HashMap::new();

    // time O(n) space: O(n)
    for n in &nums {
        *count.entry(*n).or_insert(0) += 1;
    }

    // time O(n) space: O(n)
    let mut bucket: HashMap<i32, Vec<i32>> = HashMap::new();
    for (n, c) in count.iter() {
        bucket.entry(*c).or_insert(Vec::new()).push(*n);
    }

    // time O(n) space: O(n)
    let mut top_k: Vec<i32> = Vec::new();
    for i in (1..=nums.len()).rev() {
        if let Some(vec) = bucket.get_mut(&(i as i32)) {
            while let Some(n) = vec.pop() {
                top_k.push(n);
                if top_k.len() == k as usize {
                    return top_k;
                }
            }
        }
    }
    vec![]
}