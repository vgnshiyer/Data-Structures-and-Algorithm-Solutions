pub fn run(matrix: Vec<Vec<i32>>, target: i32) -> bool {
    let rows = matrix.len();
    let cols = matrix[0].len();
    let total = rows * cols;
    let mut l = 0;
    let mut r = total - 1;

    while l < r {
        let m = (l + r) >> 1;
        if matrix[m / cols][m % cols] < target { l = m + 1; }
        else { r = m; }
    }
    matrix[r / cols][r % cols] == target
}