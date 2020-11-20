"""
No: 15
Date: 11-18-2020

Problem:
    Merge Two Sorted Lists
    Given two sorted linked lists, merge them together in ascending order and 
    return a reference to the merged list

TestCases:
    list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
    list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
    list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""


def mergeLinkedList(a, b):
    head = curr = ListNode(-1)
    while a and b:
        if a.val >= b.val:
            a, b = b, a
        curr.next = a
        curr = curr.next
        a = a.next
    if a:
        curr.next = a
    if b:
        curr.next = b
    return head.next


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


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


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


tests = [
    [[1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]],
    [[1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]],
    [[1, 1, 1, 1], [2], [1, 1, 1, 1, 2, 1]],
    [[1, 1, 1, 1], [], [1, 1, 1, 1]],
    [[], [1, 1, 1, 1], [1, 1, 1, 1]],
]

for index, test in enumerate(tests):
    try:
        a = ListToLinkedList(test[0])
        b = ListToLinkedList(test[1])
        res = LinkedListToArray(mergeLinkedList(a, b))
        assert res == test[2], "Test {}: found `[{}]`, should be `[{}]`".format(
            str(index), (toString(res)), (toString(test[2]))
        )
    except Exception as e:
        print(e)
        continue

