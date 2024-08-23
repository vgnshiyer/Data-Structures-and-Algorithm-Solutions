pub fn run(s: String) -> bool {
    let mut stack: Vec<char> = Vec::new();
    let s_chars: Vec<char> = s.chars().collect();
    for c in s_chars {
        let is_opening: bool = ['(', '[', '{'].contains(&c);
        if is_opening { stack.push(c); }
        else {
            if stack.is_empty() { return false; }
            if c == ')' && stack[stack.len() - 1] != '(' { return false; }
            if c == ']' && stack[stack.len() - 1] != '[' { return false; }
            if c == '}' && stack[stack.len() - 1] != '{' { return false; }
            if !stack.is_empty() { stack.pop(); }
        }
    }
    stack.is_empty()
}