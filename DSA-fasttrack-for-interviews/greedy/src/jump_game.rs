pub fn run(nums: Vec<i32>) -> bool {
    let mut need = -1;

    for i in (0..nums.len()).rev() {
        need += 1;
        if nums[i] >= need {
            need = 0;
        }
    }
    need == 0
}