#[derive(Debug, PartialEq, Eq, Clone)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    pub fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}