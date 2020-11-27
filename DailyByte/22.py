"""
No: 22
Date: 11-26-2020

Problem:
    ValidateCharacters
    Given a string only containing the following characters (, ), {, }, [, and ] 
    return whether or not the opening and closing characters are in a valid order.

TestCases:
    "(){}[]", return true
    "(({[]}))", return true
    "{(})", return false

Time Complexity:
    O(n)
Space Complexity:
    O(n)
"""


class Problem:
    def __init__(self, text):
        self.text = text

    def solution(self):
        text = self.text
        stack = []
        for char in text:
            if char == "(":
                stack.append("(")
            elif char == "[":
                stack.append("[")
            elif char == "{":
                stack.append("{")
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
        return True if not stack else False
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
                problem = Problem(test[0])
                res = problem.solution()
                assert res == test[1], "Test {}: found `{}`, should be `{}`".format(
                    str(index), (self.toString(res)), (self.toString(test[1]))
                )
            except Exception as e:
                print(e)


testCases = [
    ["(){}[]", True],
    ["(({[]}))", True],
    ["{(})", False],
]

test = Test(testCases)
test.run()
