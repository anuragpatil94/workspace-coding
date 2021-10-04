"""
No: 238
Date: 09-25-2021

Problem: Product of Array Except Self
    

TestCases:
    

Time Complexity:
    
Space Complexity:
    
"""


from codetest import CodeTest


class ProductOfArrayExceptSelf:
    def main(self, nums):
        """
        Description: brute-force method
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        res = []

        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    mult *= nums[j]
            res.append(mult)
        return res

    def solution2(self, nums):
        """
        Description: 2 pass from front and back. this will
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        res = []
        mult = 1
        for i in range(len(nums)):
            res.append(mult)
            mult *= nums[i]

        mult = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * mult
            mult *= nums[i]
        return res


tests = [
    {
        "params": {
            "input": [{"value": [1, 2, 3, 4]}],
            "output": [{"value": [24, 12, 8, 6]}],
        }
    },
    {
        "params": {
            "input": [{"value": [-1, 1, 0, -3, 3]}],
            "output": [{"value": [0, 0, 9, 0, 0]}],
        }
    },
    {
        "params": {
            "input": [{"value": [-1, 1, 0, -3, 0, 3]}],
            "output": [{"value": [0, 0, 0, 0, 0, 0]}],
        }
    },
    {
        "params": {
            "input": [{"value": [1, 1]}],
            "output": [{"value": [1, 1]}],
        }
    },
    {
        "params": {
            "input": [{"value": [0, 0]}],
            "output": [{"value": [0, 0]}],
        }
    },
]


c = CodeTest(tests, ProductOfArrayExceptSelf)
