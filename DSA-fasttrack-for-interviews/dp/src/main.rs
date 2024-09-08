mod climb_stairs;
mod min_cst_clmb_stairs;
mod house_robbers;
mod longest_palindrome;
mod palidromic_substr;
mod decode_ways;
mod coin_change;
mod max_product;

fn main() {
    println!("{}", climb_stairs::run(3));

    println!("{}", min_cst_clmb_stairs::run(vec![10,15,20]));

    println!("{}", house_robbers::run(vec![2,7,9,3,1]));

    println!("{}", longest_palindrome::run("babad".to_string()));

    println!("{}", palidromic_substr::run("aaa".to_string()));

    println!("{}", decode_ways::run("12".to_string()));

    println!("{}", coin_change::run(vec![2], 3));

    println!("{}", max_product::run(vec![2, 3, -2, 4]));
}
