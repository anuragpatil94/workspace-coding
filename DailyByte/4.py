"""
No: 4
Date: 11-07-2020

Problem:
    isCapitalized
    Given a string, return whether or not it uses capitalization correctly. 
    A string correctly uses capitalization if all letters are capitalized, 
    no letters are capitalized, or only the first letter is capitalized.

TestCases:
    Ex: Given the following strings...

    "USA", return true
    "Calvin", return true
    "compUter", return false
    "coding", return true

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""


def isCapitalized(str) -> bool:
    if str == str.upper():
        return True
    if str == str[0].upper() + str[1:]:
        return True
    if str == str.lower():
        return True
    return False


tests = {
    "USA": True,
    "Calvin": True,
    "compUter": False,
    "coding": True,
    "Padjkfnmclkl12 23kd adjk": True,
}
for test, result in tests.items():
    assert isCapitalized(test) == result, test + " should be " + str(not result)
