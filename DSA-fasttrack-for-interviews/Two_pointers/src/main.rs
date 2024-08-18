mod valid_palindrom;
mod two_sum_sorted_inp;
mod three_sum;
mod container_with_most_water;
mod trapping_rainwater;

fn main() {
    println!("{}", valid_palindrom::run("a.".to_string()));

    println!("{:?}", two_sum_sorted_inp::run(vec![2, 7, 11, 15], 9));

    println!("{:?}", three_sum::run1(vec![-1,0,1,2,-1,-4]));
    println!("{:?}", three_sum::run2(vec![-1,0,1,2,-1,-4]));

    println!("{}", container_with_most_water::run(vec![1,8,6,2,5,4,8,3,7]));
    println!("{}", container_with_most_water::run_alt(vec![1,8,6,2,5,4,8,3,7]));

    println!("{}", trapping_rainwater::run(vec![0,1,0,2,1,0,1,3,2,1,2,1]));
}
