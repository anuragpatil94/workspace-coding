"""
No: 9
Date: 11-12-2020

Problem:
    Jewels and Stones
    Given a string representing your stones and another string representing a 
    list of jewels, return the number of stones that you have that are also 
    jewels.

TestCases:
    jewels = "abc", stones = "ac", return 2
    jewels = "Af", stones = "AaaddfFf", return 3
    jewels = "AYOPD", stones = "ayopd", return 0

Time Complexity:
    O(n+m) where n is the length of stones and m is the length of jewels
Space Complexity:
    O(m) where m is the length of jewels
    
"""


def jewelsAndStones(stones: str, jewels: str) -> int:
    count = 0
    jewels = set(list(jewels))
    for stone in stones:
        if stone in jewels:
            count = count + 1
    return count
    pass


tests = [["ac", "abc", 2], ["AaaddfFf", "Af", 3], ["ayopd", "AYOPD", 0]]

for index, test in enumerate(tests):
    res = jewelsAndStones(test[0], test[1])
    assert res == test[2], (
        "result for test "
        + index
        + " returned as "
        + res
        + "but it should be "
        + test[2]
    )

