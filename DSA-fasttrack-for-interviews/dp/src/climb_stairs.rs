pub fn run(n: i32) -> i32 {
    let mut dp: Vec<i32> = vec![0;n as usize + 1];
    dp[n as usize] = 1;

    for i in (0..n as usize).rev() {
        dp[i] += dp[i + 1];
        if i + 2 <= n as usize { dp[i] += dp[i + 2] }
    }
    dp[0]
}