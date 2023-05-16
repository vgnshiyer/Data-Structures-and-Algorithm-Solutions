class node:
    data = 0
    nxt = None

def sumList(head1, head2, carry):
    if(head1 == None and head2 == None and carry == 0):
        return None

    sum_ = carry

    sumHead = node()
    
    if(head1 != None):
        sum_ += head1.data
        nextHead1 = head1.nxt
    else:
        nextHead1 = None

    if(head2 != None):
        sum_ += head2.data
        nextHead2 = head2.nxt
    else:
        nextHead2 = None

    newcarry = sum_ // 10
    sum_ %= 10

    sumHead.data = sum_
    
    sumHead.nxt = sumList(nextHead1, nextHead2, newcarry)

    return sumHead

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

if __name__ == '__main__':
    head1 = makeLinkedList([7, 1, 6])
    head2 = makeLinkedList([5, 9])


    sumHead = sumList(head1, head2, 0)
    printList(sumHead)