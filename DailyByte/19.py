"""
No: 19
Date: 11-22-2020

Problem:
    Given a linked list, containing unique numbers, return whether or not it 
    has a cycle.
    Note: a cycle is a circular arrangement (i.e. one node points back to 
    a previous node)

TestCases:
    1->2->3->1 -> true (3 points back to 1)
    1->2->3 -> false
    1->1 true (1 points to itself)

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""



class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Problem:
    def __init__(self, head):
        self.head = head

    def solution(self):
        head = slow = self.head
        fast = slow.next
        while fast and fast.next:
            if slow == fast or slow.next ==fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
