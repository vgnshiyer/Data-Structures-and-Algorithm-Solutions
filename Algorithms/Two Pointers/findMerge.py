
## https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?isFullScreen=true

## WHAT I LEARNT
# The idea is to make the two pointers travel the same distance in the list so that they eventually arrive at the same point which is our answer.
# The other approach could be to make the pointers travel the same distance by substracting the length of the lists. This will ensure that the pointer of the longer list 
# will travel the same distance as the shorter list pointer.

def findMergeNode(head1, head2):
    temp1 = head1
    temp2 = head2
    while temp1 != temp2:
        if temp1 == None:
            temp1 = head2
        else:
            temp1 = temp1.next
            
        if temp2 == None:
            temp2 = head1
        else:
            temp2 = temp2.next
    return temp1.data