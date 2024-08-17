pub mod valid_palindrom;
pub mod two_sum_sorted_inp;

fn main() {
    println!("{}", valid_palindrom::run("a.".to_string()));

    println!("{:?}", two_sum_sorted_inp::run(vec![2, 7, 11, 15], 9));
}
