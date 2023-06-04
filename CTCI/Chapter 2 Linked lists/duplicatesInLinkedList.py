## duplicates from a linked list

## using temp var O(n) time O(n) space

def removeDup(head):
    seen = set()

    temp = head
    while(temp.next != None):
        if temp.next.data in seen:
            temp.next = temp.next.next
        else:
            seen.add(temp.data)
    return head

## without temp arr O(n^2)

def removeDup(head):
    temp = head

    while(temp != None):
        ## search for temp
        runner = temp
        while(runner.next != None):
            if(runner.next.data == temp.data):
                runner.next = runner.next.next
            else:
                runner = runner.next
    return head