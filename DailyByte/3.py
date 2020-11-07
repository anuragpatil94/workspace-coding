"""
No: 3
Date: 11-06-2020

Problem:
    Given a string representing the sequence of moves a robot vacuum makes, 
    return whether or not it will return to its original position. 
    The string will only contain L, R, U, and D characters, 
    representing left, right, up, and down respectively.

TestCases:
    Ex: Given the following strings...

    "LR", return true
    "URURD", return false
    "RUULLDRD", return true
        
Time Complexity:
    O(n) where n is length of string
Space Complexity:
    O(1)
    
"""


def robotMovement(str):
    sum = 0
    for char in str:
        if char == "L":
            sum += -1
        if char == "R":
            sum += 1
        if char == "U":
            sum += 1
        if char == "D":
            sum += -1
    return sum == 0


assert robotMovement("LR") == True
assert robotMovement("URURD") == False
assert robotMovement("RUULLDRD") == True
