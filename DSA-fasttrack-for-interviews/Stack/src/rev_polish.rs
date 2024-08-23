pub fn run(tokens: Vec<String>) -> i32 {
    let mut stack: Vec<i32> = Vec::new();

    fn is_operand(t: &str) -> bool {
        ["+", "-", "*", "/"].contains(&t)
    }

    fn eval(op1: i32, op2: i32, op: &str) -> i32 {
        match op {
            "+" => op1 + op2,
            "-" => op1 - op2,
            "*" => op1 * op2,
            "/" => op1 / op2,
            _ => panic!("Unknown operator!")
        }
    }

    for t in tokens {
        if is_operand(&t) {
            let op1 = stack.pop().unwrap();
            let op2 = stack.pop().unwrap();
            let x = eval(op2, op1, &t);
            stack.push(x);
        } else {
            stack.push(t.parse::<i32>().unwrap());
        }
    }
    stack.pop().unwrap()
}