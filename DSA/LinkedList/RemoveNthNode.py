# Approach 1 : using 2 passes 
# 1. 1st pass find the length of the linkedlist
# 2. remove nth node 


def removeNthNode(head, n):
    length = 0

    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    if length == n:
        return head.next
    
    curr = head
    for _ in range(length - n - 1):
        curr = curr.next
    
    curr.next = curr.next.next

    return head

# Approach 2 : one pass using dummy node

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def removeNthNodeFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = None

    fast = dummy
    slow = dummy

    for _ in range(n):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next

    return dummy.next

