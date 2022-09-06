## https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true

## WHAT I LEARNT
# this is the famous hare and the tortoise problem
# also added code to remove the cyccle from the linked list
# visit this link for the algo explanation: https://www.youtube.com/watch?v=Fj1ywT9ETQk&t=656s

def has_cycle(head):
    fast = head
    slow = head
    while( fast != None and fast.next != None):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return 1
    return 0

def removeCycle(head):
    fast = head
    slow = head
    while slow != fast:
        fast = fast.next.next
        slow = slow.next
    fast = head
    while fast.next != slow.next:
        fast = fast.next
        slow = slow.next
    slow.next = None