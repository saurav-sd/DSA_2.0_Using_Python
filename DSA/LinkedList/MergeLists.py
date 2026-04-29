class ListNode:
    def __init__(self,val,next):
        self.val = val
        self.next = next

def mergeTwoLists(l1,l2):
    dummy = ListNode(0)
    dummy.next = None

    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
    
    curr.next = l1 if l1 else l2

    return dummy.next

# Time = O(N + M) | Space = O(1)