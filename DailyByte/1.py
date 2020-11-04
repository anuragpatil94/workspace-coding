"""
No: 1
Date: 2020-11-04

Problem: 
    Reverse String: Given a string, reverse all of its characters and return the resulting string.

TestCases:
    Ex: Given the following strings...
    “Cat”, return “taC”
    “The Daily Byte”, return "etyB yliaD ehT”
    “civic”, return “civic”

Time Complexity:
    O(n) where n is length of string
Space Complexity:
    O(1)
"""


def reverseString(str) -> str:
    revStr = []
    for i in range(len(str) - 1, -1, -1):
        revStr.append(str[i])
    return "".join(revStr)


assert reverseString("Cat") == "taC", "should be `taC`"
assert reverseString("The Daily Byte") == "etyB yliaD ehT", "should be `etyB yliaD ehT`"
assert reverseString("civic") == "civic", "should be `civic`"
