use std::collections::HashMap;

// time: O(n x mlogm) space: O(n)
pub fn run(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut anagram_groups: HashMap<String, Vec<String>> = HashMap::new();

    for s in strs {
        let mut s_chars: Vec<char> = s.chars().collect();
        s_chars.sort_unstable();
        let s_sorted: String = s_chars.into_iter().collect();

        anagram_groups.entry(s_sorted).or_insert(Vec::new()).push(s);
    }

    anagram_groups.into_values().collect()
}