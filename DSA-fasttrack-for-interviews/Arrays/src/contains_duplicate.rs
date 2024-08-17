use std::collections::HashSet;


// time: O(n) space: O(n)
pub fn run(nums: Vec<i32>) -> bool {
    let mut set: HashSet<i32> = HashSet::new();
    for i in nums {
        if set.contains(&i) {
            return true;
        }
        set.insert(i);
    }
    false
}