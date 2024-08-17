use std::collections::HashMap;

// time: O(nlogn) space: O(1)
pub fn run_1(s: String, t: String) -> bool {
    let mut s_chars: Vec<char> = s.chars().collect();
    let mut t_chars: Vec<char> = t.chars().collect();

    s_chars.sort_unstable() == t_chars.sort_unstable()
}

// time: O(n) space: O(n)
pub fn run_2(s: String, t: String) -> bool {
    let mut count: HashMap<char, i32> = HashMap::new();

    for c in s.chars() {
        *count.entry(c).or_insert(0) += 1;
    }

    for c in t.chars() {
        let counter = count.entry(c).or_insert(0);
        *counter -= 1;
        if *counter == 0 {
            count.remove(&c);
        }
    }

    count.is_empty()
}