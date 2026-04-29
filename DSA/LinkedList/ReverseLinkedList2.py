class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    for _ in range(left-1):
        prev = prev.next

    curr = prev.next

    # Reversal logic : Take next node and insert at front
    for _ in range(right-left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next

node6 = ListNode(6)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

reverse = reverseBetween(node1,2,4)

