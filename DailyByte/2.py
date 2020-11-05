"""
No: 2
Date: 11-05-2020

Problem:
    Palindrome
    Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
    Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

TestCases:
    Ex: Given the following strings...

    "level", return true
    "algorithm", return false
    "A man, a plan, a canal: Panama.", return true

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""


def isPalindrome(str) -> bool:
    str = str.lower()

    i, j = 0, len(str) - 1
    while i < j:
        a = ord(str[i])
        b = ord(str[j])

        if (97 <= a <= 122) and (97 <= b <= 122):
            if a == b:
                i += 1
                j -= 1
            else:
                return False
        else:
            if not (97 <= a <= 122):
                i += 1
            if not (97 <= b <= 122):
                j -= 1
    return True


assert (isPalindrome("level")) == True
assert (isPalindrome("helaosdfijaosdnkncmnkzxh")) == False
assert (isPalindrome("als,.sh,.17,.dh,l.dlh.2.1.2d h s s l a")) == True
assert (isPalindrome("A man, a plan, a canal: Panama.")) == True
