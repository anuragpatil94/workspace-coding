"""
No: 6
Date: 11-09-2020

Problem:
    Given an array of strings, return the longest common prefix that is shared amongst all strings.
    Note: you may assume all strings only contain lowercase alphabetical characters.

TestCases:
    Ex: Given the following arrays...

    ["colorado", "color", "cold"], return "col"
    ["a", "b", "c"], return ""
    ["spot", "spotty", "spotted"], return "spot"

Time Complexity:
    O(n) where n is total number of words 
Space Complexity:
    O(n) where n in total number of words
    
"""

# Using Trie
class Trie:
    def __init__(self):
        self.dict = {}
        self.numWords = 0

    def add(self, string):
        self.numWords += 1
        current = self.dict
        for char in string:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[-1] = True

    def display(self):
        print(self.dict)

    def common(self):
        current = self.dict
        commonIndex = 0
        string = ""
        while True:
            if len(current) == 1:
                commonIndex += 1
                for letter in current:
                    string += letter
                    current = current[letter]
                    break
            elif -1 in current or len(current) != 1:
                return string


tests = [
    [["colorado", "color", "cold"], "col"],
    [["a", "b", "c"], ""],
    [["spot", "spotty", "spotted"], "spots"],
]


for index, test in enumerate(tests):
    t = Trie()
    for word in test[0]:
        t.add(word)
    toBeAsserted = t.common()
    assert (
        toBeAsserted == test[1]
    ), "common letters in test {} is `{}` but found `{}`".format(
        index, test[1], toBeAsserted
    )

