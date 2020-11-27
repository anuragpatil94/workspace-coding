"""
No: 24
Date: 11-27-2020

Problem:
    Given a string s containeing only lowercase letters, continuously remove 
    adjacent characterts that are teh smae adn return the result.

TestCases:
    s = "abccba", return ""
    s = "foobar", return "fbar"
    s = "abccbefggfe", return "a"

Time Complexity:
    
Space Complexity:
    
"""
import traceback


class Problem:
    def __init__(self, text):
        self.text = text

    def solution(self):
        text = self.text
        stack = []
        for char in text:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


class Test:
    def __init__(self, tests: list):
        self.tests = tests
        pass

    def toString(self, variable, delimeter=","):
        print(type(variable), variable)
        if isinstance(variable, str):
            return variable
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
                # print(traceback.format_exc())


testCases = [
    ["abccba", ""],
    ["foobar", "fbar"],
    ["abccbefggfe", "ae"],
]

test = Test(testCases)
test.run()
