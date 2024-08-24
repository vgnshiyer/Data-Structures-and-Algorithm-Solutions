mod binary_search;
mod search_in_2D;

fn main() {
    println!("{}", binary_search::run(vec![-1,0,3,5,9,12], 9));

    println!("{}", search_in_2D::run(vec![vec![1,3,5,7],vec![10,11,16,20],vec![23,30,34,60]], 8));
}
