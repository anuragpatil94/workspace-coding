"""
No: 18
Date: 11-21-2020

Problem:
    Mid of Linked List
    Given a non-empty linked list, return the middle node of the list. If the 
    linked list contains an even number of elements, return the node closer to the end.

TestCases:
    1->2->3->null, return 2
    1->2->3->4->null, return 3
    1->null, return 1

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
        head = slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val


class Test:
    def __init__(self, tests: list):
        self.tests = tests
        pass

    def listToLinkedList(self, arr):
        head = curr = ListNode(None)
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return head.next

    def linkedListToArray(self, l):
        arr = []
        while l:
            arr.append(l.val)
            l = l.next
        return arr

    def toString(self, variable, delimeter=","):
        if isinstance(variable, str):
            return str
        elif isinstance(variable, list):
            for index, val in enumerate(variable):
                variable[index] = self.toString(val)
            return delimeter.join(variable)
        elif isinstance(variable, int):
            # int, long,float,complex
            return str(variable)
        # tuple set dictionary
        pass

    def run(self):
        tests = self.tests
        for index, test in enumerate(tests):
            try:
                a = self.listToLinkedList(test[0])
                problem = Problem(a)
                res = problem.solution()
                assert res == test[1], "Test {}: found `[{}]`, should be `[{}]`".format(
                    str(index), (self.toString(res)), (self.toString(test[1]))
                )
            except Exception as e:
                print(e)


testCases = [
    [[1, 2, 3], 2],
    [[8, 1, 1, 4, 2], 1],
    [[7, 12, 2, 9], 2],
    [[7, 12, 2, 5, 6, 9], 5],
    [[7], 7],
]

test = Test(testCases)
test.run()
