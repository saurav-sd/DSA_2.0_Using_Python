# Approach 1 : Using array 
# 1. convert list to array
# 2. partation
# 3. convert back to linkedlist
# Time = O(N) | Space = O(N)

# Approach 2 : Using dummy nodes iterative method 
# make dummy nodes for before and after partation

def partation(head, x):
    before = ListNode(0)
    after = ListNode(0)

    before_curr = before
    after_curr = after

    curr = head

    while curr:
        if curr.val < x:
            before_curr.next = curr
            before_curr = before_curr.next
        else:
            after_curr.next = curr
            after_curr = after_curr.next
        
        curr = curr.next
    
    after_curr.next = None
    before_curr.next = after.next

    return before.next
    


