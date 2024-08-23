pub fn run(n: i32) -> Vec<String> {
    let mut result: Vec<String> = Vec::new();
    fn dfs(a: i32, b: i32, t: String, result: &mut Vec<String>) {
        if b < a || a < 0 || b < 0 { return; }
        if a == 0 && b == 0 { 
            result.push(t);
            return;
        }
        dfs(a - 1, b, t.clone() + "(", result);
        dfs(a, b - 1, t.clone() + ")", result);
    }
    dfs(n, n, "".to_string(), &mut result);
    result
}