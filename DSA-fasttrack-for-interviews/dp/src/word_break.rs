pub fn run(s: String, word_dict: Vec<String>) -> bool {
    let mut dp: Vec<bool> = vec![false; s.len() + 1];
    dp[0] = true;
    for i in 0..s.len() {
        if dp[i] {
            for word in &word_dict {
                if i + word.len() <= s.len() && &s[i..i + word.len()] == word {
                    dp[i + word.len()] = true;
                }
            }
        }
    }
    dp[s.len()]
}