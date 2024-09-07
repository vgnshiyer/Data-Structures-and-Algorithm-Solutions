struct MaxPal {
    pal: String,
    len: i32
}

impl MaxPal {
    fn new(pal: String, len: i32) -> Self {
        MaxPal {
            pal: pal,
            len: len,
        }
    }
}

pub fn run(s: String) -> String {
    // state: dp[i][j] = is s[i][j] palindrome
    // transition: dp[i][j] = 1 if dp[i+1][j-1] is 1 and s[i] == s[j]
    // base: dp[i][i] = 1

    let s_chars: Vec<char> = s.chars().collect();
    let n = s.len();
    let mut dp: Vec<Vec<i32>> = vec![vec![0;n];n];
    for i in 0..n { dp[i][i] = 1; }
    let mut mp = MaxPal::new(s_chars[0].to_string(), 1);

    for i in (0..n).rev() {
        for j in i+1..n {
            if s_chars[i] == s_chars[j] {
                if j == i + 1 { dp[i][j] = 1; }
                else { dp[i][j] = dp[i+1][j-1]; }
            }
            if dp[i][j] == 1 {
                if j - i + 1 > mp.len as usize {
                    mp.pal = s_chars[i..j+1].into_iter().collect();
                    mp.len = (j - i + 1) as i32;
                }
            }
        }
    }
    mp.pal
}