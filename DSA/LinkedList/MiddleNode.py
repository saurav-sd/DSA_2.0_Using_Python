# Approach 1 : using 2 passes
# 1. count total nodes
# 2. Traverse again to n//2

def middleNode(head):
    n = 0
    curr = head

    while curr:
        n =+ 1
        curr = curr.next

    curr = head
    for _ in range(n // 2):  # _ : It tells anyone reading your code (and the Python interpreter): "I need to loop a certain number of times, but I don't actually care about the index number
        curr = curr.next

    return curr

# Time = O(N) + O(N) = O(N) | Space = O(1)

# Approach 2: using fast and slow pointer

def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    return slow

# Time = O(N) | O(1)