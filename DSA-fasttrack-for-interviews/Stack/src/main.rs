mod valid_parenthesis;
mod min_stack;
mod rev_polish;
mod gen_parenthesis;

fn main() {
    println!("{}", valid_parenthesis::run("()".to_string()));

    println!("{}", rev_polish::run(vec![
        "4".to_string(),
        "13".to_string(),
        "5".to_string(),
        "/".to_string(),
        "+".to_string()
    ]));

    println!("{:?}", gen_parenthesis::run(3));
}
