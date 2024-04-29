"""Utility functions for working with Linked Lists."""
    
from __future__ import annotations
    
__author__ = "730544766"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return the data attribute for the first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return a linked list of every element minus the head."""
        return self.next
    
    def last(self) -> int:
        """Return the data of the last element in the linked list."""
        while 0 < 1:
            if self.next is not None:
                self = self.next
            else:
                return self.data
        return self.data
    

def value_at(head: Node | None, index: int) -> int:
    """Finds the data value of a specified node."""
    if index == 0 and head is not None:  
        return head.data
    elif head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        return value_at(head.next, index - 1)
    

def max(head: Node | None) -> int:
    """Finds the largest data value in the list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.data
    else:
        if head.data > head.next.data:
            return head.data
    return max(head.next)


def linkify(items: list[int]) -> Node | None:
    """Returns nodes with certain values."""
    if len(items) == 0:
        return None
    else:
        return Node(items[0], linkify(items[1:]))
    

def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a scaled linked list of Nodes."""
    if head is None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))