mod climb_stairs;
mod min_cst_clmb_stairs;
mod house_robbers;
mod longest_palindrome;
mod palidromic_substr;

fn main() {
    println!("{}", climb_stairs::run(3));

    println!("{}", min_cst_clmb_stairs::run(vec![10,15,20]));

    println!("{}", house_robbers::run(vec![2,7,9,3,1]));

    println!("{}", longest_palindrome::run("babad".to_string()));

    println!("{}", palidromic_substr::run("aaa".to_string()));
}
