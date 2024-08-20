use std::collections::{HashMap, HashSet};

// time: O(n ^ 2) space: O(n)
pub fn run(s: String) -> i32 {
    let mut freq: HashMap<char, i32> = HashMap::new();
    let s_chars: Vec<char> = s.chars().collect();
    let mut l = 0;

    fn is_all_unique(f: &HashMap<char, i32>) -> bool {
        for v in f.values() {
            if *v > 1 {
                return false;
            }
        }
        true
    }

    let mut answer = 0;
    for r in 0..s_chars.len() {
        *freq.entry(s_chars[r]).or_insert(0) += 1;
        while !is_all_unique(&freq) {
            if let Some(count) = freq.get_mut(&s_chars[l]) {
                *count -= 1;
            }
            l += 1;
        }
        answer = answer.max(r - l + 1);
    }
    answer as i32
}


// my original previous approach checks the entire hashmap again and again..
// we can just check if the latest is already in the hashmap or not and pop elements from the left.
// time: O(n) space: O(n)
pub fn run_alt(s: String) -> i32 {
    let mut seen: HashSet<char> = HashSet::new();
    let s_chars: Vec<char> = s.chars().collect();
    let mut l = 0;
    let mut answer = 0;
    for r in 0..s_chars.len() {
        while seen.contains(&s_chars[r]) {
            seen.remove(&s_chars[l]);
            l += 1;
        }
        answer = answer.max(r - l + 1);
        seen.insert(s_chars[r]);
    }
    answer as i32
}