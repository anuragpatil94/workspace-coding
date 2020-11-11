"""
No: 8
Date: 11-11-2020

Problem:
    Two Sum
    Given an array of integers, return whether or not two numbers sum to a given 
    target, k.
    Note: you may not sum a number with itself.

TestCases:
    [1, 3, 8, 2], k = 10, return true (8 + 2)
    [3, 9, 13, 7], k = 8, return false
    [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

Time Complexity:
    O(n) - length of array
Space Complexity:
    O(n) - length of array
    
"""


def TwoSum(arr, k) -> bool:
    dict = {}
    for num in arr:
        if (num) not in dict:
            dict[k - num] = num
        else:
            return True
    return False


tests = [
    [[1, 3, 8, 2], 10, True],
    [[3, 9, 13, 7], 8, False],
    [[4, 2, 6, 5, 2], 4, True],
]

for test in tests:
    assert TwoSum(test[0], test[1]) == test[2]

