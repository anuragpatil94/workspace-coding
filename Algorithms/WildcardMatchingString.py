"""
Given a string and pattern. Find if the string matches the pattern
if the pattern has
 - ?  any one char allowed
 - *  0 or more sequence
"""


def WildCardMatching(string, pattern):
    np = " "
    found = 0
    for char in pattern:
        if char == "*" and not found:
            np += char
            found = 1
        elif char != "*":
            np += char
            found = 0

    pattern = np
    string = " " + string
    res = [[0] * (len(pattern)) for i in range(len(string))]

    # Init
    res[0][0] = 1
    if pattern[1] == "*":
        res[0][1] = 1

    for i in range(1, len(string)):
        for j in range(1, len(pattern)):
            si = i
            pj = j
            if string[si] == pattern[pj] or pattern[pj] == "?":
                res[i][j] = res[i - 1][j - 1]
            elif pattern[pj] == "*":
                res[i][j] = res[i][j - 1] or res[i - 1][j]

    return res[-1][-1]


tests = [
    ["xaylmz", "x?y*z", True],
    ["anvyhdleq", "*h?l**", True],
    ["anvyhdleq", "???y*hd?eq", True],
    ["anvyhdleq", "a*?hdleq", True],
    ["anvyhdleq", "a*h?dleq", False],
]

for test in tests:
    assert WildCardMatching(test[0], test[1]) == test[2]

