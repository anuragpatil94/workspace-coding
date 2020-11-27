"""
No: 23
Date: 11-26-2020

Problem:
    Given two strings s and t, which represents a sequence of keystrokes, where
    # denotes a backspace, return whether or not the sequences produce the same 
    result.

TestCases:
    s = "ABC#", t = "CD##AB", return true
    s = "como#pur#ter", t = "computer", return true
    s = "cof#dim#ng", t = "code", return false

Time Complexity:
    O(s+t)
Space Complexity:
    O(s+t)
"""


class Problem:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def solution(self):
        s = self.text1
        t = self.text2

        def finalString(text):
            stack = []
            for char in text:
                if char != "#":
                    stack.append(char)
                else:
                    stack.pop()
            return "".join(stack)

        s = finalString(s)
        t = finalString(t)
        return s == t
        pass


class Test:
    def __init__(self, tests: list):
        self.tests = tests
        pass

    def toString(self, variable, delimeter=","):
        if isinstance(variable, str):
            return str
        elif isinstance(variable, list):
            for index, val in enumerate(variable):
                variable[index] = self.toString(val)
            return delimeter.join(variable)
        elif isinstance(variable, int):
            # int, long,float,complex
            return str(variable)
        # tuple set dictionary
        pass

    def run(self):
        tests = self.tests
        for index, test in enumerate(tests):
            try:
                problem = Problem(test[0], test[1])
                res = problem.solution()
                assert res == test[2], "Test {}: found `{}`, should be `{}`".format(
                    str(index), (self.toString(res)), (self.toString(test[2]))
                )
            except Exception as e:
                print(e)


testCases = [
    ["ABC#", "CD##AB", True],
    ["como#pur#ter", "computer", True],
    ["cof#dim#ng", "code", False],
]

test = Test(testCases)
test.run()
