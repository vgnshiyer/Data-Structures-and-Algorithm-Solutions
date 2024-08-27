use crate::cmn::ListNode;

pub fn run(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    match (list1, list2) {
        (None, None) => None,
        (None, Some(l2)) => Some(l2),
        (Some(l1), None) => Some(l1),
        (Some(mut l1), Some(mut l2)) => {
            if l1.val < l2.val {
                l1.next = run(l1.next.take(), Some(l2));
                Some(l1)
            } else {
                l2.next = run(Some(l1), l2.next.take());
                Some(l2)
            }
        }
    }
}