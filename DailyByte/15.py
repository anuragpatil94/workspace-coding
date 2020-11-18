"""
No: 15
Date: 11-18-2020

Problem:
    Given two sorted linked lists, merge them together in ascending order and 
    return a reference to the merged list

TestCases:
    list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
    list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
    list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null

Time Complexity:
    
Space Complexity:
    
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
