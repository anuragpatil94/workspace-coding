"""
No: 21
Date: 11-24-2020

Problem:
    Given a linked list, containing unique values, reverse it, and return the result.

TestCases:
    1->2->3->null, return a reference to the node that contains 3 which points 
    to a list that looks like the following: 3->2->1->null
    7->15->9->2->null, return a reference to the node that contains 2 which 
    points to a list that looks like the following: 2->9->15->7->null
    1->null, return a reference to the node that contains 1 which points 
    to a list that looks like the following: 1->null

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""


class Problem:
    def __init__(self, head):
        self.head = head

    def solution(self):
        head = self.head
        cur = head
        prev = None
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        return prev


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


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
                res = self.linkedListToArray(problem.solution())

                assert res == test[1], "Test {}: found `[{}]`, should be `[{}]`".format(
                    str(index), (self.toString(res)), (self.toString(test[1]))
                )
            except Exception as e:
                print(e)


testCases = [
    [[1, 2, 3], [3, 2, 1]],
    [[1, 2, 3, 4], [4, 3, 2, 1]],
    [[7], [7]],
    [[], []],
]

test = Test(testCases)
test.run()
