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
}
