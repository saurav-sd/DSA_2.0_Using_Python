# Remove Linked List Elements

# Approach 1 : iteration without dummy

def removeElements(head, val):
    while head and head.val == val:
        head = head.next
    
    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head

# Approach 2 : using dummy node
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeElement(head, val):
    dummy = ListNode(0)
    dummy.next = head

    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return dummy.next

# Time = O(N) | Space = O(1)