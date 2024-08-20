use std::cmp::min;

pub fn run(height: Vec<i32>) -> i32 {
    let mut mono: Vec<usize> = Vec::new();
    let mut water_held = 0;
    let n = height.len();
    for i in 0..n {
        while !mono.is_empty() && height[i] > height[mono[mono.len() - 1]] {
            let p = height[mono.pop().unwrap()];
            if mono.is_empty() {
                break;
            }
            let p_minus_1 = height[mono[mono.len() - 1]];
            water_held += (min(p_minus_1, height[i]) - p) * (i - mono[mono.len() - 1] - 1) as i32;
        }
        mono.push(i);
    }
    water_held
}