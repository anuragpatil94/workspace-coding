"""
No: 1
Date: 11-04-2020

Problem:
    Add two numbers as a linked list
    You are given two linked-lists representing two non-negative integers. 
    The digits are stored in reverse order and each of their nodes contain a single digit. 
    Add the two numbers and return it as a linked list.

TestCases:
    Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

Time Complexity:
    O(n)
Space Complexity:
    O(n)
    
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def count(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def equalLengths(self, l1, l2):
        c1, c2 = l1, l2
        len1 = self.count(c1)
        len2 = self.count(c2)

        if len1 != len2:
            if len2 < len1:
                l1, l2 = l2, l1
                i = 0
                x = None
                while i < len2 - len1:
                    y = ListNode(0)
                    if x:
                        x.next = y
                        y = y.next
                    else:
                        x = y
                        newhead = x
                    i += 1
                x.next = l1
                l1 = newhead
        return l1, l2

    def addTwoNumbers(self, l1, l2, c=0):
        l1, l2 = self.equalLengths(l1, l2)

        def req(l1, l2, c):
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            c.next, cur_carry = ListNode((a + b) % 10), (a + b) // 10
            if l1.next and l2.next:
                a = l1.next if l1.next else 0
                b = l2.next if l2.next else 0
                carry = req(a, b, c.next)
                c.next.val += carry

                return cur_carry
            else:
                return 0

        out = ListNode(-1)
        carry = req(l1, l2, out)
        if carry:
            newhead = ListNode(carry)
            newhead.next = out.next
        else:
            newhead = out.next

        return newhead

    def addTwoNumbersWithReversedNumbers(self, l1, l2, c=0):
        l1, l2 = self.equalLengths(l1, l2)

        def req(a, b, c=0):
            if not a and not b:
                return a
            a.val, carry = c + (a.val + b.val) % 10, (a.val + b.val) // 10
            req(a.next, b.next, carry)
            return a

        return req(l1, l2)


l1 = ListNode(2)
l1.next = ListNode(7)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(8)
l2.next.next = ListNode(2)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val),
    result = result.next

l1 = ListNode(2)
l1.next = ListNode(7)
l1.next.next = ListNode(4)
# 4 5 6
l2 = ListNode(1)
l2.next = ListNode(8)
l2.next.next = ListNode(2)
result = Solution().addTwoNumbersWithReversedNumbers(l1, l2)
while result:
    print(result.val),
    result = result.next
# 3 5 7

