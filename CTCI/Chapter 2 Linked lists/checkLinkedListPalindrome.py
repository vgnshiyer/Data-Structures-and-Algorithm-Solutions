## check linked list palindrome

class node:
    data = 0
    nxt = None

def checkPalindrome(head) -> bool:
    if(head == None):
        return False
    if(head.nxt == None):
        return True
    
    listLength = length(head)

    mid = getMiddle(head)

    part1 = head

    ## instead of computing the length of the list, you could just check if the fast pointer is at a Null node or not
    ## Null Node => odd length / else => even length
    if(listLength % 2 == 1):
        part2 = reverse(mid.nxt)
    else:
        part2 = reverse(mid)

    return compare(part1, part2)

def compare(part1, part2) -> bool:
    while(part1 != None and part2 != None):
        if part1.data != part2.data:
            return False
        part1 = part1.nxt
        part2 = part2.nxt
    return True

def getMiddle(head):
    slow, fast = head, head
    while(fast != None and fast.nxt != None):
        fast = fast.nxt.nxt
        slow = slow.nxt
    return slow

def reverse(head):
    if(head.nxt == None or head == None):
        return head

    newHead = reverse(head.nxt)
    head.nxt.nxt = head
    head.nxt = None
    return newHead

def makeLinkedList(nums):
    head = node()
    head.data = nums[0]

    temp = head
    for i in range(1, len(nums)):
        newnode = node()
        newnode.data = nums[i]
        temp.nxt = newnode
        temp = temp.nxt

    return head

def printList(head):
    while(head != None):
        print(head.data)
        head = head.nxt

def length(head):
    l = 0
    while(head != None):
        l += 1
        head = head.nxt
    return l

if __name__ == '__main__':
    head1 = makeLinkedList([0,1,2,1,0])
    head2 = makeLinkedList([0,1,1,0])
    head3 = makeLinkedList([0,1,2,3])

    print(checkPalindrome(head1))
    print(checkPalindrome(head2))
    print(checkPalindrome(head3))