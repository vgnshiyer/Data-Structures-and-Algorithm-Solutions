use std::collections::HashMap;

struct window {
    elements: HashMap<char, i32>,
    max_freq: i32
}

impl window {
    pub fn new() -> Self {
        window {
            elements: HashMap::new(),
            max_freq: 0
        }
    }

    pub fn add(&mut self, c: char) {
        *self.elements.entry(c).or_insert(0) += 1;
        self.max_freq = self.max_freq.max(*self.elements.get(&c).unwrap());
    }

    pub fn get_max_freq(&self) -> i32 {
        self.max_freq
    }

    pub fn remove(&mut self, c: char) {
        *self.elements.entry(c).or_insert(0) -= 1;
    }
}

pub fn run(s: String, k: i32) -> i32 {
    // window_len - max_freq > k --> remove from left
    let mut window = window::new();
    let s_chars: Vec<char> = s.chars().collect();
    let mut answer: i32 = 0;
    let mut l = 0;
    for r in 0..s_chars.len() {
        window.add(s_chars[r]);
        while (r - l + 1) as i32 - window.get_max_freq() > k {
            // it's not required to update the max_freq value as
            // even it changes, it can never be a value greater
            // than the previous greatest value.
            // therefore it is OKAY to let it stay old.
            window.remove(s_chars[l]);
            l += 1;
        }
        answer = answer.max((r - l + 1) as i32);
    }
    answer
}