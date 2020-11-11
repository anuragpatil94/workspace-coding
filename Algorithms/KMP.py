"""
No: NA
Date: 11-11-2020

Problem:
    KMP Search Algorithm: 
        Try to find all the matches for a given pattern and return its index

TestCases:
    

Time Complexity:
    O(n+m) where n is the length of pattern and m is the length of the text
Space Complexity:
    O(n) where n is the length of pattern
"""


def KMP(text, pattern):
    prefix = [0] * len(pattern)
    i, j = 0, 1

    # create prefix array of pattern
    while j < len(pattern):
        if pattern[j] == pattern[i]:
            prefix[j] = i + 1
            i += 1
            j += 1
        else:
            # rollback if letters don't match
            while i >= 0:
                if pattern[j] == pattern[prefix[i - 1]]:
                    i = prefix[i - 1] + 1
                    prefix[j] = i
                    j += 1
                    break
                else:
                    if i == 0:
                        prefix[j] = 0
                        j += 1
                        break
                    i = prefix[i - 1]
    indexLocations = []

    # To keep track of the result while iterating
    count = 0
    i, j = 0, 0

    # Compare text with pattern using prefix array
    while j < len(text) and i < len(pattern):
        # letter matches the pattern
        if text[j] == pattern[i]:
            count += 1
            # This will help rollback to find multiple instances of the pattern
            # in the string
            if count == len(pattern):
                indexLocations.append(j - len(pattern) + 1)
                j = j - prefix[i] + 1
                i = 0
                count = 0
            else:
                i += 1
                j += 1
        else:
            while i >= 0:
                # letter matches the pattern after rollback
                if text[j] == pattern[prefix[i - 1]]:
                    i = prefix[i - 1] + 1
                    count = i
                    j += 1
                    break
                else:
                    # break when i == 0 and continue
                    if i == 0:
                        count = 0
                        j += 1
                        break
                    i = prefix[i - 1]
    return indexLocations

tests = [
    ["abxabcabcabyabxabcabcaby", "abcaby", [6, 18]],
    ["abyabcabyabcaby", "abyabcaby", [0, 6]],
]

for test in tests:
    assert KMP(test[0], test[1]) == test[2]

