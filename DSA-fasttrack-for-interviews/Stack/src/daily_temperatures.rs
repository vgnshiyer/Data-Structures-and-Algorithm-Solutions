/// We maintain a monotonic stack in decreasing order.
/// while current element is bigger than the top of stack, we pop
/// Since those elements are smaller than the current and dont matter to us.
pub fn run(temperatures: Vec<i32>) -> Vec<i32> {
    let mut result: Vec<i32> = Vec::new();
    let mut mono: Vec<usize> = Vec::new();
    for i in (0..temperatures.len()).rev() {
        while !mono.is_empty() && temperatures[*mono.last().unwrap()] <= temperatures[i] { mono.pop(); }
        result.push(
            if mono.is_empty() { 0 }
            else { (*mono.last().unwrap() - i).try_into().unwrap() }
        );
        mono.push(i);
    }
    result.reverse();
    result
}