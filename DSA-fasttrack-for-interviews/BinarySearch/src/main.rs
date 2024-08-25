mod binary_search;
mod search_in_2_d;
mod koko_eating_bananas;

fn main() {
    println!("{}", binary_search::run(vec![-1,0,3,5,9,12], 9));

    println!("{}", search_in_2_d::run(vec![vec![1,3,5,7],vec![10,11,16,20],vec![23,30,34,60]], 8));

    println!("{}", koko_eating_bananas::run(vec![3,6,7,11], 8));
}
