pub fn run(s: String) -> i32 {
    let n = s.len();
    let mut dp: Vec<i32> = vec![0; n + 1];
    dp[n] = 1;

    for i in (0..n).rev() {
        let onedigit: i32 = s[i..i+1].parse().unwrap();
        if onedigit >= 1 && onedigit <= 9 {
            dp[i] += dp[i + 1];
        }
        if i < n - 1 {
            let twodigit: i32 = s[i..i+2].parse().unwrap();
            if twodigit >= 10 && twodigit <= 26 {
                dp[i] += dp[i + 2];
            }
        }
    }
    dp[0]
}