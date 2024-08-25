pub fn run(nums: Vec<i32>) -> i32 {
    let mut l = 0;
    let mut r = nums.len() - 1;
    while l < r {
        let m = (l + r) >> 1;
        if nums[m] > *nums.last().unwrap() { l = m + 1; }
        else { r = m; }
    }
    nums[r]
}