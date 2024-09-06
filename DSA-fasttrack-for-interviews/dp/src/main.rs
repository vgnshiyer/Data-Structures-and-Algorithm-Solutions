mod climb_stairs;
mod min_cst_clmb_stairs;

fn main() {
    println!("{}", climb_stairs::run(3));

    println!("{}", min_cst_clmb_stairs::run(vec![10,15,20]));
}
