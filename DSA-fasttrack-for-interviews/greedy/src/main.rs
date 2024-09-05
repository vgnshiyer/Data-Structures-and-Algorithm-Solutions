mod max_sum_subarr;
mod jump_game;
mod jump_game2;

fn main() {
    println!("{}", max_sum_subarr::run(vec![-2,1,-3,4,-1,2,1,-5,4]));

    println!("{}", jump_game::run(vec![2,3,1,1,4]));

    println!("{}", jump_game2::run(vec![2,3,1,1,4]));
}
