pub fn run(nums: Vec<i32>, target: i32) -> i32 {
    fn bs(start: usize, end: usize, target: i32, nums: &Vec<i32>) -> usize {
        let mut l = start;
        let mut r = end;
        while l < r {
            let m = (l + r) >> 1;
            if nums[m] < target { l = m + 1; }
            else { r = m; }
        }
        r
    }

    fn get_min_pt(nums: &Vec<i32>) -> usize {
        let mut l = 0;
        let mut r = nums.len() - 1;
        while l < r {
            let m = (l + r) >> 1;
            if nums[m] > *nums.last().unwrap() { l = m + 1; }
            else { r = m; }
        }
        r
    }

    let m = get_min_pt(&nums);

    if m > 0 {
        let left_half = bs(0, m - 1, target, &nums);
        if nums[left_half] == target {
            return left_half as i32;
        }
    }

    let right_half = bs(m, nums.len() - 1, target, &nums);
    if nums[right_half] == target {
        return right_half as i32;
    }
    -1
}