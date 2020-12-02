"""
No: 30
Date: 12-02-2020

Problem:
    Given the reference to the root of a binary search tree and a search value, 
    return the reference to the node that contains the value if it exists and 
    null otherwise.
    Note: all values in the binary search tree will be unique.

TestCases:
    

Time Complexity:
    
Space Complexity:
    
"""


def findValue(root, val):
    cur = root
    q = [cur]
    while q:
        cur = q.pop(0)
        if cur.val == val:
            return cur
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return None

