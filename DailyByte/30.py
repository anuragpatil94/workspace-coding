"""
No: 30
Date: 12-03-2020

Problem:
    Given a binary search tree, rearrange the tree such that it forms a linked 
    list where all its values are in ascending order.

TestCases:
    

Time Complexity:
    
Space Complexity:
    
"""


def inOrder(node):
    arr = []

    def _inorder(node, arr):
        if not node:
            return
        _inorder(node.left, arr)
        arr.append(node.val)
        _inorder(node.right, arr)

    _inorder(node, arr)
    # Arr to Linked List
    listNode = []
    for num in arr:
        listNode.append(num)

