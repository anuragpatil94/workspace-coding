"""
No: 11
Date: 11-14-2020

Problem:
    First Unique Character
    Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

TestCases:
    "abcabd", return 2
    "thedailybyte", return 1
    "developer", return 0

Time Complexity:
    O(n)
Space Complexity:
    O(n)
    
"""


def firstUniqueCharacter(text: str) -> int:
    x = {}

    for char in text:
        if char in x:
            x[char] += 1
        else:
            x[char] = 1

    for index, char in enumerate(text):
        if x[char] == 1:
            return index


tests = [
    ["abcabd", 2],
    ["thedailybyte", 1],
    ["developer", 0],
]

for index, test in enumerate(tests):
    res = firstUniqueCharacter(test[0])
    assert res == test[1], "Result for test {} is {}, but it should be {}".format(
        index, str(res), str(test[1])
    )

