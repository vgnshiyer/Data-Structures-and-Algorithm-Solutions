pub fn run(s: String) -> i32 {
    let schars: Vec<char> = s.chars().collect();
    let n = s.len();
    let mut dp: Vec<Vec<i32>> = vec![vec![0;n];n];
    for i in 0..n { dp[i][i] = 1; }
    let mut count: i32 = n as i32;

    for i in (0..n).rev() {
        for j in i+1..n {
            if schars[i] == schars[j] {
                if j == i + 1 { dp[i][j] = 1; }
                else {
                    if dp[i+1][j-1] == 1 {
                        dp[i][j] = 1;
                    }
                }
            }
            count += dp[i][j];
        }
    }
    count
}