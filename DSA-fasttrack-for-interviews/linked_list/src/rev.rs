struct ListNode {
    val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

pub fn run(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    fn reverse(
        curr: Option<Box<ListNode>>,
        prev: Option<Box<ListNode>>
    ) -> Option<Box<ListNode>> {
        match curr {
            Some(mut node) => {
                let next = node.next;
                node.next = prev;
                reverse(next, Some(node))
            }
            None => prev,
        }
    }
    reverse(head, None)
}