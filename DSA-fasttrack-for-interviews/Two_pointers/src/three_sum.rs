// time: O(nlogn + n ^ 3) space: O(1)
pub fn run1(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut nums = nums;
    nums.sort_unstable();
    let n = nums.len();
    let mut result: Vec<Vec<i32>> = Vec::new();
    for i in 0..n {
        if i > 0 && nums[i] == nums[i-1] { continue; }
        for j in i+1..n {
            if j-1 != i && nums[j] == nums[j-1] { continue; }
            for k in j+1..n {
                if k-1 != j && nums[k] == nums[k-1] { continue; }
                if nums[i] + nums[j] + nums[k] == 0 {
                    result.push(vec![nums[i], nums[j], nums[k]]);
                }
            }
        }
    }
    result
}

// time: O(nlogn + n ^ 2) space: O(1)
pub fn run2(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut nums = nums;
    nums.sort_unstable();
    let n = nums.len();
    let mut result: Vec<Vec<i32>> = Vec::new();
    for i in 0..n {
        if i > 0 && nums[i] == nums[i - 1] { continue; }
        let mut j = i + 1;
        let mut k = n - 1;
        while j < k {
            let sum = nums[i] + nums[j] + nums[k];
            if sum < 0 {
                j += 1;
            } else if sum > 0 {
                k -= 1
            } else {
                result.push(vec![nums[i], nums[j], nums[k]]);
                j += 1;
                k -= 1;
                while j > 0 && j < k && nums[j] == nums[j - 1] { j += 1; }
                while k < n - 1 && j < k && nums[k] == nums[k + 1] { k -= 1; }
            }
        }
    }
    result
}