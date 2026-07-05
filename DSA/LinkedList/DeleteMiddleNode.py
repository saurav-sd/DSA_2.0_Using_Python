# using slow and fast pointer - one pass solution.

def deleteMiddleNode(head):
    if not head.next:
        return None
    
    slow = head
    fast = head
    prev = None

    while fast or fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head

