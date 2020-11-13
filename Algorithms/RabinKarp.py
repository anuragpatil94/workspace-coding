"""
    Rabin Karp Algorithm
        - Following algorithm doesn't work on overlapping substring match.
    Hashing:
        hash(str) = ascii(str[0]) * prime**0 + ascii(str[1]) * prime**1 +...
"""


def RabinKarp(text, pattern):
    prime = 227

    def hash(text, i, j, prevHash=0):
        substring = text[i:j]
        hash = prevHash
        if not hash:
            for index, char in enumerate(substring):
                hash += ord(char) * (prime ** index)
        else:
            hash = ((hash - ord(text[i - 1])) // prime) + (
                ord(text[j - 1]) * prime ** (len(substring) - 1)
            )
        return hash

    res = []
    i = 0
    j = len(pattern)
    hashOfPattern = hash(pattern, i, j, 0)
    currentHash = 0
    while j <= len(text):
        current = text[i:j]
        currentHash = hash(text, i, j, currentHash)
        if currentHash == hashOfPattern:
            k = 0
            while k < len(current):
                if current[k] == pattern[k]:
                    if k == len(current) - 1:
                        res.append(i)
                    k += 1
                else:
                    break
            i += k
            j += k
        else:
            i += 1
            j += 1
    return res


tests = [
    ["abeda", "eda", [2]],
    ["abxabcabcabyabxabcabcaby", "abcaby", [6, 18]],
    ["abyabcabyabcaby", "abyabcaby", [0]],
]

for test in tests:
    assert RabinKarp(test[0], test[1]) == test[2]
