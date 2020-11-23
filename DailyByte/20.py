"""
No: 20
Date: 11-23-2020

Problem:
    Given a potentially cyclical linked list where each value is unique, 
    return the node at which the cycle starts. If the list does not contain 
    a cycle, return null.

TestCases:
    1->2->3, return null
    1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
    1->9->3->7->7 (7 points to itself), return a reference to the node containing 7

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""


def startOfCycle(head):
    # end cases
    if not head:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        if not fast:
            return -1
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next

    # Visualize this with a example
    slow = slow.next
    fast = head

    # Once we know that there is a cycle then we move fast back to start because
    # the distance from start to start of cycle is same as slow to start of cycle
    while slow != fast:
        if not slow or not fast:
            return None
        slow = slow.next
        fast = fast.next

    return slow
