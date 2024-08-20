use std::{collections::HashMap, f32::INFINITY};

struct Window {
    f: HashMap<char, i32>,
    w: Vec<char>,
    m: usize
}

impl Window {
    fn new() -> Self {
        Window {
            f: HashMap::new(),
            w: Vec::new(),
            m: INFINITY as usize
        }
    }

    fn add(&mut self, c: char) {
        *self.f.entry(c).or_insert(0) += 1;
    }

    fn remove(&mut self, c: char) {
        *self.f.entry(c).or_insert(0) -= 1;
    }

    fn good(&self) -> bool {
        for v in self.f.values() { if *v > 0 { return false; } }
        true
    }

    fn update(&mut self, len: usize, substr: Vec<char>) {
        if len < self.m {
            self.m = len;
            self.w = substr;
        }
    }
}

// time: O(n x 26) space: O(n)
pub fn run(s: String, t: String) -> String {
    let s_chars: Vec<char> = s.chars().collect();
    let t_chars: Vec<char> = t.chars().collect();
    let mut window = Window::new();
    for c in &t_chars { window.add(*c); }

    let mut l = 0;
    for r in 0..s_chars.len() {
        window.remove(s_chars[r]);
        while window.good() {
            window.update(r - l + 1, s_chars[l..=r].to_vec());
            window.add(s_chars[l]);
            l += 1;
        }
    }
    window.w.iter().collect()
}