"""
No: 5
Date: 11-08-2020

Problem:
    Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
    Note: neither binary string will contain leading 0s unless the string itself is 0

TestCases:
    Ex: Given the following binary strings...

    "100" + "1", return "101"
    "11" + "1", return "100"
    "1" + "0", return  "1"
    
Time Complexity:
    O(n) where n is the length of max(num1,num2)
Space Complexity:
    O(1) for space other than result.
    
"""


def binarySum(num1, num2) -> str:
    result = ""
    carry = 0

    len1 = len(num1)
    len2 = len(num2)
    if len2 < len1:
        num1, num2 = num2, num1
        len1, len2 = len2, len1
    num1 = "0" * (len2 - len1) + num1

    for i in range(len(num1) - 1, -1, -1):
        sum = int(num1[i]) + int(num2[i]) + carry
        if sum > 2:
            sum = 1
            carry = 1
        elif sum > 1:
            sum = 0
            carry = 1
        else:
            carry = 0
        result = str(sum) + result
    if carry:
        result = str(carry) + result
    return result
    pass


tests = [
    ["100", "1", "101"],
    ["11", "1", "100"],
    ["1", "0", "1"],
    ["101010", "01101110", "10011000"],
]
for test in tests:
    assert binarySum(test[0], test[1]) == test[2], "Sum should be " + str(test[2])

