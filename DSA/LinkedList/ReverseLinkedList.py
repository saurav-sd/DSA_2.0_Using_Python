# Reverse linked list


# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach1 : Bruteforce approach
# 1. store values in array
# 2. reverse array
# 3. Rebuild List


def reverseList_Bruteforce(head):
    arr = []

    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next

    curr = head
    for val in reversed(arr):
        curr.val = val
        curr = curr.next

    return head


# Approach 2 : In place Reversal(Optimised)
def reverseList_iterative(head):
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # store next
        curr.next = prev  # reverse link
        prev = curr  # move prev
        curr = next_temp  # move curr

    return prev

# Approach 3 : Recurssive
def reverseList_recurssive(head):
    # base case
    if not head or not head.next:
        return head
    
    new_head = reverseList_recurssive(head.next)

    head.next.next = head
    head.next = None

    return new_head


# ---------------------------
# create List :  1 -> 2 -> 3
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

result = reverseList_Bruteforce(node1)
print("Reversed Linkedlist : ", result)
