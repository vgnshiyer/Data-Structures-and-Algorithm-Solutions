use std::cmp;

pub fn run(s1: String, s2: String) -> i32 {
    // state: dp[i][j] -> longest common subseq ending at i and j
    // transition: dp[i][j] = 1 + dp[i + 1][j + 1] if s1[i] == s[j] else max(dp[i + 1][j], dp[i][j + 1])
    // base: dp[_][_] = 0

    let mut dp: Vec<Vec<i32>> = vec![vec![0;s2.len() + 1];s1.len() + 1];
    let mut max_len: i32 = 0;

    for i in (0..s1.len()).rev() {
        for j in (0..s2.len()).rev() {
            if s1.chars().nth(i) == s2.chars().nth(j) {
                dp[i][j] = 1 + dp[i+1][j+1];
            } else {
                dp[i][j] = cmp::max(dp[i+1][j], dp[i][j+1]);
            }
            max_len = max_len.max(dp[i][j]);
        }
    }
    max_len
}