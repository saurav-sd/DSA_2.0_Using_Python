# Approach : 
# 1. use dummy node
# 2. find kth node.
# 3. Reverse Group

class ListNode:
    def __init__(self,bal,next):
        self.val = self.val
        self.next = next

def reverseKgroup(head, k):
    dummy = ListNode(0)
    dummy.next = head

    group_prev = dummy

    while True:
        kth = group_prev

        # find the kth node
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
            
        group_next = kth.next

        # reverse group
        prev = group_next
        curr = group_prev.next

        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # reconnect
        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp