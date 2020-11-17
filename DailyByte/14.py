"""
No: 14
Date: 11-17-2020

Problem:
Uncommon Words
    Given two strings representing sentences, return the words that are not 
    common to both strings (i.e. the words that only appear in one of the 
    sentences). You may assume that each sentence is a sequence of words 
    (without punctuation) correctly separated using space characters.

TestCases:
    sentence1 = "the quick", 
    sentence2 = "brown fox", 
    return ["the", "quick", "brown", "fox"]
    
    sentence1 = "the tortoise beat the haire", 
    sentence2 = "the tortoise lost to the haire", 
    return ["beat", "to", "lost"]
    
    sentence1 = "copper coffee pot", 
    sentence2 = "hot coffee pot", 
    return ["copper", "hot"]

Time Complexity:
    O(n+m) where n and m are length of text
Space Complexity:
    O(n+m) where n and m are length of text
    
"""


def uncommonWords(s1, s2):
    count = set()
    banned = set()
    for word in s1.split(" "):
        count.add(word)
    for word in s2.split(" "):
        if word in count:
            count.remove(word)
            banned.add(word)
        else:
            if word not in banned:
                count.add(word)

    return sorted(list(count))


tests = [
    ["the quick", "brown fox", sorted(["the", "quick", "brown", "fox"])],
    [
        "the tortoise beat the haire",
        "the tortoise lost to the haire",
        sorted(["beat", "to", "lost"]),
    ],
    ["copper coffee pot", "hot coffee pot", sorted(["copper", "hot"])],
]

for index, test in enumerate(tests):
    res = uncommonWords(test[0], test[1])
    assert res == test[2], "Test {}: found `{}`, should be `{}`".format(
        index, res, test[2]
    )
