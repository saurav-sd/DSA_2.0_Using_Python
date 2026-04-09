# Approach 1 : Bruteforce using set

def hasCycle_Bruteforce(head):
    visited = set()

    curr = head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False

# Time  = O(N) | Space = O(N)

# Approach 2 : using slow fast pointer

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

# Time = O(N) | Space = O(1)