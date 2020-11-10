"""
No: 7
Date: 11-10-2020

Problem:
    Given a string and the ability to delete at most one character, 
    return whether or not it can form a palindrome.
    Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

TestCases:
    "abcba", return true
    "foobof", return true (remove the first 'o', the second 'o', or 'b')
    "abccab", return false

Time Complexity:
    O(n) 
Space Complexity:
    O(n) - n number of recursions
"""


def isPalindrome(str, maximumAllowedToRemove):
    def checkPalindrome(left, right, n):
        if left == right or left > right:
            return True
        if str[left] == str[right]:
            left += 1
            right -= 1
            return checkPalindrome(left, right, n)
        else:
            n -= 1
            return n >= 0 and (
                checkPalindrome(left + 1, right, n)
                or checkPalindrome(left, right - 1, n)
            )

    return checkPalindrome(0, len(str) - 1, maximumAllowedToRemove)


assert isPalindrome("abcba", 1) == True
assert isPalindrome("foobof", 2) == True
assert isPalindrome("abccab", 1) == False
