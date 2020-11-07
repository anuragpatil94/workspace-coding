"""
No: 2
Date: 11-07-2020

Problem:
    Longest Substring without Repeating Characters
    Given a string, find the length of the longest substring without repeating characters.

TestCases:
    abrkaabcdefghijjxxx == 10
    "abcabcbb" == 3
    "" == 0
    "abcabcabcabc" == 3
    "dabcabcbb" == 4
    "aaaaaaaabc" == 3
    "aaaaaaaaaa" == 1
    "abcdefgh" == 8
    "pwwkew" == 3

Time Complexity:
    O(n) where n is number of characters
Space Complexity:
    O(n) where n is number of characters
    
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        longest = 0
        i = 0
        j = 0

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
            else:
                longest = max(j - i, longest)
                while i <= j:
                    if s[i] != s[j]:
                        seen.remove(s[i])
                        i += 1
                    else:
                        i += 1
                        j += 1
                        break
        longest = max(j - i, longest)
        return longest


print(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"))
# 10

tests = {
    "abrkaabcdefghijjxxx": 10,
    "abcabcbb": 3,
    "": 0,
    "abcabcabcabc": 3,
    "dabcabcbb": 4,
    "aaaaaaaabc": 3,
    "aaaaaaaaaa": 1,
    "abcdefgh": 8,
    "pwwkew": 3,
}
for test, result in tests.items():
    assert Solution().lengthOfLongestSubstring(test) == result, (
        test + " should be " + str(result)
    )
