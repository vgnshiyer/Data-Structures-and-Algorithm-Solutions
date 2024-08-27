use crate::cmn::ListNode;

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