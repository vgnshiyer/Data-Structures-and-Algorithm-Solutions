mod climb_stairs;
mod min_cst_clmb_stairs;
mod house_robbers;
mod longest_palindrome;
mod palidromic_substr;
mod decode_ways;
mod coin_change;
mod max_product;
mod word_break;
mod longest_incr_subseq;
mod partition_eq_subset_sum;
mod longest_cmn_subseq;
mod coin_change2;

mod buy_and_sell_stocks;
mod buy_and_sell_stocks2;
mod buy_and_sell_stocks3;
mod buy_and_sell_stocks4;
mod buy_and_sell_stocks5;

mod target_sum;
mod interleaving_str;

fn main() {
    println!("{}", climb_stairs::run(3));

    println!("{}", min_cst_clmb_stairs::run(vec![10,15,20]));

    println!("{}", house_robbers::run(vec![2,7,9,3,1]));

    println!("{}", longest_palindrome::run("babad".to_string()));

    println!("{}", palidromic_substr::run("aaa".to_string()));

    println!("{}", decode_ways::run("12".to_string()));

    println!("{}", coin_change::run(vec![2], 3));

    println!("{}", max_product::run(vec![2, 3, -2, 4]));

    println!("{}", word_break::run("catsandog".to_string(), vec!["cats".to_string(), "and".to_string(), "dog".to_string()]));

    println!("{}", longest_incr_subseq::run(vec![10,9,2,5,3,7,101,18]));

    println!("{}", partition_eq_subset_sum::run(vec![100,100,100,100,100,100,100,100]));

    println!("{}", longest_cmn_subseq::run("abcde".to_string(), "ace".to_string()));

    println!("{}", coin_change2::run(5, vec![1,2,5]));

    println!("{}", buy_and_sell_stocks::run(vec![7,1,5,3,6,4]));

    println!("{}", buy_and_sell_stocks2::run(vec![7,1,5,3,6,4]));

    println!("{}", buy_and_sell_stocks3::run(vec![3,3,5,0,0,3,1,4]));

    println!("{}", buy_and_sell_stocks4::run(2, vec![2,4,1]));

    println!("{}", buy_and_sell_stocks5::run(vec![1,2,3,0,2]));

    println!("{}", target_sum::run(vec![1,1,1,1,1], 3));

    println!("{}", interleaving_str::run("aabcc".to_string(), "dbbca".to_string(), "aadbbcbcac".to_string()));
}
