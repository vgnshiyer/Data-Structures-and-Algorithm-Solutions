use std::collections::HashMap;

// time: O(n ^ 26) space: O(n)
pub fn run(s1: String, s2: String) -> bool {
    let mut f: HashMap<char, i32> = HashMap::new();
    let s1_chars: Vec<char> = s1.chars().collect();
    let s2_chars: Vec<char> = s2.chars().collect();

    for c in &s1_chars { *f.entry(*c).or_insert(0) += 1; }
    
    let mut l = 0;

    fn all_present(f: &HashMap<char, i32>) -> bool {
        for v in f.values() { if *v > 0 { return false; } }
        true
    }

    for r in 0..s2_chars.len() {
        *f.entry(s2_chars[r]).or_insert(0) -= 1;
        while all_present(&f) {
            if (r - l + 1) == s1_chars.len() { return true; }
            *f.get_mut(&s2_chars[l]).unwrap() += 1;
            l += 1;
        }
    }
    false
}