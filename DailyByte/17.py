"""
No: 17
Date: 11-20-2020

Problem:
    Remove Value
    Given a linked list and a value, remove all nodes containing the provided 
    value, and return the resulting list.

TestCases:
    1->2->3->null, value = 3, return 1->2->null
    8->1->1->4->12->null, value = 1, return 8->4->12->null
    7->12->2->9->null, value = 7, return 12->2->9->null

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""


def removeNodesWithValue(head, value):
    h = curr = ListNode("$")
    curr.next = head

    while curr.next:
        if curr.next.val == value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return h.next


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
    [[1, 2, 3], 3, [1, 2]],
    [[8, 1, 1, 4, 2], 1, [8, 4, 2]],
    [[7, 12, 2, 9], 7, [12, 2, 9]],
    [[7, 12, 2, 9], 9, [7, 12, 2]],
]

for index, test in enumerate(tests):
    try:
        a = ListToLinkedList(test[0])
        b = test[1]
        res = LinkedListToArray(removeNodesWithValue(a, b))
        assert res == test[2], "Test {}: found `[{}]`, should be `[{}]`".format(
            str(index), (toString(res)), (toString(test[2]))
        )
    except Exception as e:
        print(e)
        continue
