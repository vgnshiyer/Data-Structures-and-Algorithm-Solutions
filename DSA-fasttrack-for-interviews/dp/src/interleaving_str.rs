use std::collections::HashMap;

pub fn run(s1: String, s2: String, s3: String) -> bool {
    if s1.len() + s2.len() != s3.len() { return false; }

    let s1_chars: Vec<char> = s1.chars().collect();
    let s2_chars: Vec<char> = s2.chars().collect();
    let s3_chars: Vec<char> = s3.chars().collect();

    let mut memo: HashMap<(usize, usize), bool> = HashMap::new();

    fn helper(s1: &Vec<char>, s2: &Vec<char>, s3: &Vec<char>, i: usize, j: usize, memo: &mut HashMap<(usize, usize), bool>) -> bool {
        if i >= s1.len() && j >= s2.len() { return true; }

        if let Some(val) = memo.get(&(i, j)) {
            return *val
        }

        if i < s1.len() && s1[i] == s3[i + j] { 
            if helper(s1, s2, s3, i + 1, j, memo) { 
                memo.insert((i, j), true);
                return true;
            }
        }
        if j < s2.len() && s2[j] == s3[i + j] { 
            if helper(s1, s2, s3, i, j + 1, memo) { 
                memo.insert((i, j), true);
                return true;
            }
        }
        memo.insert((i, j), false);
        false
    }
    
    helper(&s1_chars, &s2_chars, &s3_chars, 0, 0, &mut memo)
}