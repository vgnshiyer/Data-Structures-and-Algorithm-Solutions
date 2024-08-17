use std::collections::HashMap;

// time: O(n) space: O(n)
pub fn run(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut tracker: HashMap<i32, i32> = HashMap::new();

    for (i, n) in nums.iter().enumerate() {
        let need = target - n;
        if tracker.contains_key(&need) {
            return vec![tracker[&need], i.try_into().unwrap()];
        }
        tracker.insert(*n, i.try_into().unwrap());
    }
    vec![-1, -1]
}