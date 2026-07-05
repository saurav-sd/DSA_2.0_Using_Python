# Approach 1 : rotate node by node repeat k times 
# Time = O(n * k)

# Approach 2 : Optimal (cyclic Trick)
# 1. find the length
# 2. make the LL circular
# 3. normalize the k
# 4. find the new tail. tail = k - 1
# 5. break the cycle

def rotateRight(head):
    if not head or not head.next or k == 0:
        return head
    
    length = 0
    curr = head

    while curr.next:
        curr = curr.next
        length += 1

    curr.next = head

    k = k % 10

    step = length - k
    new_tail = head

    for _ in range(step - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head

# Time = O(n) | Space = O(1)