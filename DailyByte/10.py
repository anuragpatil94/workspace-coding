"""
No: 10
Date: 11-13-2020

Problem:
    Valid Anagram
    Given two strings s and t return whether or not s is an anagram of t.
    Note: An anagram is a word formed by reordering the letters of another word.

TestCases:
    s = "cat", t = "tac", return true
    s = "listen", t = "silent", return true
    s = "program", t = "function", return false

Time Complexity:
    
Space Complexity:
    
"""


def validAnagram(s, t):
    if len(s) != len(t):
        return False
    unique = 0
    charMap = {}
    for char in s:
        if char in charMap:
            charMap[char] += 1
        else:
            charMap[char] = 1
            unique += 1

    for char in t:
        if char in charMap and charMap[char] > 0:
            charMap[char] -= 1
            if charMap[char] == 0:
                unique -= 1
        else:
            return False

    return False if unique else True


tests = [
    ["cat", "tac", True],
    ["catt", "taac", True],
    ["listen", "silent", True],
    ["program", "function", False],
]

for index, test in enumerate(tests):
    res = validAnagram(test[0], test[1])
    assert res == test[2], "The result of test {} should be {} but found {}".format(
        index, str(test[2]), str(res)
    )

