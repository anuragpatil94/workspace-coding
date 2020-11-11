"""
Given a string and pattern. Find if the string matches the pattern
if the pattern has
 - ?  any one char allowed
 - *  0 or more sequence
"""


def WildCardMatching(string, pattern):
    np = ""
    found = 0
    # Remove continuous * from the pattern
    for char in pattern:
        if char == "*" and not found:
            np += char
            found = 1
        elif char != "*":
            np += char
            found = 0

    # Adding a space before the string so that the string index starts with 1
    pattern = " " + np
    string = " " + string

    # init 2D array
    res = [[0] * (len(pattern)) for i in range(len(string))]

    # defaults for the result
    # since " " and " " from pattern and string are equal
    res[0][0] = 1
    # Only if 1st letter in the pattern is *. Hardcode res to 1 because we don't
    # traverse i=0 or j=0
    if pattern[1] == "*":
        res[0][1] = 1

    # Main Algorithm
    for i in range(1, len(string)):
        for j in range(1, len(pattern)):
            if string[i] == pattern[j] or pattern[j] == "?":
                res[i][j] = res[i - 1][j - 1]
            elif pattern[j] == "*":
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

