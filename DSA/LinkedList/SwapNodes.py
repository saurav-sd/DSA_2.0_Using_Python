# bruteforce approach : value swap
def swapNodesValue(head):
    curr = head

    while curr and curr.next:
        curr.val, curr.next.val = curr.next.val, curr.val

        curr = curr.next.next
    return head

# Iterative Pointer Manipulation
class ListNode:
    def __init__(self,val,next):
        self.val = val
        self.next = next

def nodeNodes(head):
    dummy = ListNode(0)
    dummy.next = head

    curr = dummy

    while curr.next and curr.next.next:
        first = curr.next
        second = curr.next.next

        #swap
        first.next = second.next
        second.next = first
        curr.next = second

        #move forward
        curr = first
        
    return dummy.next


