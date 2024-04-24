"""Code from lesson 28 video."""


from __future__ import annotations

class Node:
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        self.data = data
        self.next = next


my_node: Node = Node(9, None)
my_other_node: Node = Node(8, my_node)
my_other_other_node: Node = Node(4, my_other_node)


print(my_other_other_node.next.next.next)