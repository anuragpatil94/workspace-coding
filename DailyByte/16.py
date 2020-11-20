"""
No: 16
Date: 11-20-2020

Problem:
    Remove Nth to Last Node
    Given a linked list and a value n, remove the nth to last node and 
    return the resulting list.
TestCases:
    1->2->3->null, n = 1, return 1->2->null
    1->2->3->null, n = 2, return 1->3->null
    1->2->3->null, n = 3, return 2->3->null

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""


def RemoveNthToLastNode(head, n):
    slow = fast = head

    while n > 0:
        fast = fast.next
        n -= 1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    if slow == head:
        return head.next

    if slow.next:
        slow.next = slow.next.next

    return head

    pass


def ListToLinkedList(arr):
    head = curr = ListNode(None)
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return head.next


def LinkedListToArray(l):
    arr = []
    while l:
        arr.append(l.val)
        l = l.next
    return arr


def toString(variable, delimeter=","):
    if isinstance(variable, str):
        return str
    elif isinstance(variable, list):
        for index, val in enumerate(variable):
            variable[index] = toString(val)
        return delimeter.join(variable)
    elif isinstance(variable, int):
        # int, long,float,complex
        return str(variable)
    # tuple set dictionary
    pass


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


tests = [
    [[1, 2, 3], 1, [1, 2]],
    [[1, 2, 3, 4, 5], 5, [2, 3, 4, 5]],
    [[1, 2, 3, 4, 5], 2, [1, 2, 3, 5]],
]

for index, test in enumerate(tests):
    try:
        a = ListToLinkedList(test[0])
        b = test[1]
        res = LinkedListToArray(RemoveNthToLastNode(a, b))
        assert res == test[2], "Test {}: found `[{}]`, should be `[{}]`".format(
            str(index), (toString(res)), (toString(test[2]))
        )
    except Exception as e:
        print(e)
        continue
