use std::cmp::min;

// time: O(n) space: O(1)
pub fn run(height: Vec<i32>) -> i32 {
    let mut i = 0;
    let mut j = height.len() - 1;
    let mut max_water_held: i32 = 0;
    while i < j {
        let water_held = (j - i) as i32 * min(height[i], height[j]);
        max_water_held = max_water_held.max(water_held);
        if height[i] < height[j] { i += 1; }
        else { j -= 1; }
    }
    max_water_held
}

// time: O(maxh ^ 2) space: O(n)
pub fn run_alt(height: Vec<i32>) -> i32 {
    let mut mono: Vec<usize> = Vec::new();
    let n = height.len();
    let mut max_water_held = 0;
    for i in 0..n {
        for j in &mono {
            let water_held = (i - j) as i32 * min(height[i], height[*j]);
            max_water_held = max_water_held.max(water_held);
        }
        if mono.is_empty() || height[mono[mono.len() - 1]] < height[i] {
            mono.push(i);
        }
    }
    max_water_held
}