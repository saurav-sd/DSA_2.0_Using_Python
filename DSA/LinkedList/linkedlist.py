# Usage of LinkedList
# LRU Cache (browser history, caching)
# Music playlist navigation
# Undo/Redo operations
# OS memory management


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.value))
            curr = curr.next
        return "->".join(result) + "-> None"


# head = LinkedListNode(10, LinkedListNode(20, LinkedListNode(30)))

node3 = LinkedListNode(3)
node2 = LinkedListNode(2, node3)
node1 = LinkedListNode(1, node2)

print(node1)
