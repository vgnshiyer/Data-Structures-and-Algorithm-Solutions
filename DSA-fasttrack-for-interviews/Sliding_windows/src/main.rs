mod best_time_to_buy_stonks;
mod longest_substr_without_rpting_chars;
mod longest_repting_char_replcement;
mod permutation_in_string;
mod min_window_substr;
mod sliding_window_max;

fn main() {
    println!("{}", best_time_to_buy_stonks::run(vec![7, 1, 5, 3, 6, 4]));

    println!("{}", longest_substr_without_rpting_chars::run_alt("pwwkew".to_string()));

    println!("{}", longest_repting_char_replcement::run("ABAB".to_string(), 2));

    println!("{}", permutation_in_string::run("ab".to_string(), "eidbaooo".to_string()));

    println!("{}", min_window_substr::run("ADOBECODEBANC".to_string(), "ABC".to_string()));

    println!("{:#?}", sliding_window_max::run(vec![1,3,-1,-3,5,3,6,7], 3));
}
