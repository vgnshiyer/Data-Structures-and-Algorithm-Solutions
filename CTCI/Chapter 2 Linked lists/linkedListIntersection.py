## linked list intersection

def findIntersection(head1, head2):
    if not head1 or not head2:
        return None

    pt1, pt2 = head1, head2
    while pt1 not is pt2:
        pt1 = pt1.next if pt1 else head2
        pt2 = pt2.next if pt2 else head1
    return pt1