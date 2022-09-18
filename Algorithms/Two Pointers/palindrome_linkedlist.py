## Given a linked list, find whether it is a palindrome or not.
## example 1 -> 2 -> 2 -> 1 is a palindrome

def reverse(head):
    prev = None
    curr = head
    
    while(curr != None):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def getMiddle(head):
    hare = head
    tortoise = head
    
    while(hare != None and hare.next != None):
        hare = hare.next.next
        tortoise = tortoise.next
        
    return tortoise

def isPalindrome(head):
    middle = getMiddle(head)
    secondhalfstart = reverse(middle.next)
    
    firsthalfstart = head
    while(secondhalfstart != None):
        if(secondhalfstart.val != firsthalfstart.val) return False
        
        secondhalfstart = secondhalfstart.next
        firsthalfstart = firsthalfstart.next
        
    return True