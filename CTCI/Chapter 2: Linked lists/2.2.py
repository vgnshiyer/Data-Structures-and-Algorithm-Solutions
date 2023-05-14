## 2.2 kth to last

## iterative
def kthToLast(head, k):
    p1 = head
    p2 = head
    for i in range(k):
        p2 = p2.next

    while(p2 != None):
        p1 = p1.next
        p2 = p2.next

    return p1

## recursive
index = 0

def kthToLast(head, k):
    if(head == None):
        return None

    kthToLast(head.next, k)
    index += 1
    if index == k:
        return head
