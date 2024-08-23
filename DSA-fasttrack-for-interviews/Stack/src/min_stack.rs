const INFINITY: i32 = i32::MAX;

struct MinStack {
    stack: Vec<(i32, i32)>,
    cur_min: i32,
}

impl MinStack {
    fn new() -> Self {
        MinStack {
            stack: Vec::new(),
            cur_min: INFINITY,
        }
    }

    fn push(&mut self, val: i32) {
        let prev_min = self.cur_min;
        self.cur_min = self.cur_min.min(val);
        self.stack.push((val, prev_min));
    }

    fn pop(&mut self) {
        if let Some((_, prev)) = self.stack.pop() {
            self.cur_min = prev;
        }
    }

    fn top(&self) -> i32 {
        self.stack.last().map_or(0, |&(e, _)| e)
    }

    fn get_min(&self) -> i32 {
        self.cur_min
    }
}