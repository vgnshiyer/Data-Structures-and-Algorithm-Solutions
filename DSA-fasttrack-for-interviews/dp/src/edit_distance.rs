use std::{cmp::min, collections::HashMap};

pub fn run(word1: String, word2: String) -> i32 {
    let mut memo: HashMap<(usize, usize), i32> = HashMap::new();
    fn helper(s1: &Vec<char>, s2: &Vec<char>, i: usize, j: usize, memo: &mut HashMap<(usize, usize), i32>) -> i32 {
        if i >= s1.len() && j >= s2.len() { return 0; }
        if i >= s1.len() { return (s2.len() - j) as i32; }
        if j >= s2.len() { return (s1.len() - i) as i32; }

        if let Some(val) = memo.get(&(i, j)) { return *val; }

        if s1[i] == s2[j] { return helper(s1, s2, i + 1, j + 1, memo); }

        let careful_add = |a: i32, b: i32| -> i32 {
            a.checked_add(b).unwrap_or(i32::MAX)
        };
        let ret = min(
        min(
                careful_add(helper(s1, s2, i + 1, j, memo), 1),
                careful_add(helper(s1, s2, i, j + 1, memo), 1),
            ),
            careful_add(helper(s1, s2, i + 1, j + 1, memo), 1),
        );
        memo.insert((i, j), ret);
        ret
    }
    helper(&word1.chars().collect(), &word2.chars().collect(), 0, 0, &mut memo)
}