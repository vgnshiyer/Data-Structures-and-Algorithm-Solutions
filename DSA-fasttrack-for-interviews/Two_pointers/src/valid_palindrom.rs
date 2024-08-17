pub fn run(s: String) -> bool {
    let s_chars: Vec<char> = s.chars().collect();
    let mut i: isize = 0;
    let mut j: isize = (s.len() - 1) as isize;
    while i < j {
        while i < j && !s_chars[i as usize].is_alphanumeric() { i += 1; }
        while i < j && !s_chars[j as usize].is_alphanumeric() { j -= 1; }
        if s_chars[i as usize].to_lowercase().to_string() != s_chars[j as usize].to_lowercase().to_string() { return false; }
        i += 1;
        j -= 1;
    }
    true
}