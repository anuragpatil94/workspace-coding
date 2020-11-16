"""
No: 13
Date: 11-16-2020

Problem:
    Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

TestCases:
    nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
    nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
    nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []

Time Complexity:
    O(n+m) where n and m are the size of 2 arrays
Space Complexity:
    O(n) where n is number of intersected elements
"""


def intersect(arr1, arr2):
    r = set()
    s1 = set(arr1)
    for num in arr2:
        if num in s1:
            r.add(num)
    return list(r)


tests = [
    [[2, 4, 4, 2], [2, 4], [2, 4]],
    [[1, 2, 3, 3], [3, 3], [3]],
    [[2, 4, 6, 8], [1, 3, 5, 7], []],
]

for index, test in enumerate(tests):
    res = intersect(test[0], test[1])
    assert res == test[2], "Test {}: found `{}`, should be `{}`".format(
        index, res, test[2]
    )
