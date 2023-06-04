def deleteMiddle(node):
    ## copy next node data to current node
    node.data = node.next.data

    node.next = node.next.next

if __name__ == '__main__':
    deleteMiddle(node)