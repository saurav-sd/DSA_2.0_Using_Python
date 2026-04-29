# Approach 1 : Using array 

def isPalindrome(head):
    arr = []

    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr == arr[::-1]

# Time = O(N) | Space = O(N)

# Approach 2 : using fast and slow pointer + Reversal.

def iaPalindrome(head):
    # 1. find middle 
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse second half
    prev = None
    curr = slow # slow is point to middle node
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # 3. compare both halves
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True

# Time = O(N) | Space = O(1)

