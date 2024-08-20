use std::f32::INFINITY;

// time: O(n) space: O(1)
pub fn run(prices: Vec<i32>) -> i32 {
    // buy low, sell high
    let mut min_price = INFINITY as i32;
    let mut max_price = 0;
    for p in prices {
        min_price = min_price.min(p);
        max_price = max_price.max(p - min_price);
    }
    max_price
}