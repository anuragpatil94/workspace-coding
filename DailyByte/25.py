"""
No: 25
Date: 11-28-2020

Problem:
    Greater Elements
    Given two arrays of numbers, where the first array is a subset of the second
    array, return an array containing all the next greater elements for each 
    element in the first array, in the second array. If there is no greater 
    element for any element, output -1 for that number.

TestCases:
    nums1 = [4,1,2], 
    nums2 = [1,3,4,2], 
    return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the 
    first number in nums2 greater than 1, and no element in nums2 is greater 
    than 2.

    nums1 = [2,4], 
    nums2 = [1,2,3,4], 
    return [3, -1] because 3 is the first greater element that occurs in nums2 
    after 2 and no element is greater than 4.

Time Complexity:
    
Space Complexity:
    
"""


class Problem:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def solution(self):
        arr1 = self.arr1
        arr2 = self.arr2
        ans = []
        for num1 in arr1:
            flag = False
            for num2 in arr2:
                if num1 == num2:
                    flag = True
                if flag and num2 > num1:
                    ans.append(num2)
                    flag = False
                    break
            # Check if flag is true that means the value was found but no
            # greater element
            if flag:
                ans.append(-1)
        return ans
        pass


class Test:
    def __init__(self, tests: list):
        self.tests = tests
        pass

    def toString(self, variable, delimeter=","):
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
                problem = Problem(test[0], test[1])
                res = problem.solution()
                assert res == test[2], "Test {}: found `{}`, should be `{}`".format(
                    str(index), (self.toString(res)), (self.toString(test[2]))
                )
            except Exception as e:
                print(e)
                # print(traceback.format_exc())


testCases = [
    [[4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]],
    [[2, 4], [1, 2, 3, 4], [3, -1]],
]

test = Test(testCases)
test.run()
