## circular loop in a linked list

def findBeginningOfCircle(head):
    slow, fast = head, head

    ## find the circular loop
    while slow != fast:
        slow = slow.next
        fast = fast.next.next if fast.next else return None

    ## bring one of the pointers back to the start
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
