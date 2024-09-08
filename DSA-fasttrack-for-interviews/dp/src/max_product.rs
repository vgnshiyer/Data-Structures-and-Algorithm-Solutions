use std::cmp;

pub fn run(nums: Vec<i32>) -> i32 {
    let mut maxp = -11;
    let mut minp = 11;
    let mut max_product: i32 = -11;
    for i in 0..nums.len() {
        if nums[i] < 0{
            let tmp = maxp;
            maxp = minp;
            minp = tmp;
        }
        maxp = cmp::max(nums[i], maxp * nums[i]);
        minp = cmp::min(nums[i], minp * nums[i]);
        max_product = max_product.max(maxp);
    }
    max_product
}