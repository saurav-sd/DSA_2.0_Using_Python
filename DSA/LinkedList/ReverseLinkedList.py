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


# What happens if you remove next_temp?
# If you remove next_temp, you will lose the reference to the next node in the original list.
# --> This means that once you reverse the link for the current node, you won't be able to access the next node to continue the reversal process. As a result, the linked list will become disconnected, and you won't be able to reverse the entire list correctly. The reversal process relies on having access to the next node before changing the current node's next pointer, so removing next_temp would break this logic and lead to an incomplete reversal.

# What happens if you return head instead of prev?
# --> If you return head instead of prev, you will not get the correct reversed linked list. The head variable still points to the original head of the list, which is now the tail of the reversed list. The prev variable, on the other hand, points to the new head of the reversed list after the reversal process is complete. Returning head would give you a reference to the old head (now tail), while returning prev gives you a reference to the new head of the reversed list, which is what you want.