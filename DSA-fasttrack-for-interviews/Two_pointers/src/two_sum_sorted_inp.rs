// time: O(n) space: O(1)
pub fn run(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut i = 0;
    let mut j = numbers.len() - 1;

    while i < j {
        let sum = numbers[i] + numbers[j];
        if sum < target {
            i += 1;
        } else if sum > target  {
            j -=1;
        } else {
            return vec![(i + 1) as i32, (j + 1) as i32];
        }
    }
    vec![-1, -1]
}