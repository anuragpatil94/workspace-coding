"""
No: 575
Date: 11-10-2020

Problem:
    Implement a 2D iterator class. It will be initialized with an array of arrays, 
    and should implement the following methods:
    next(): returns the next element in the array of arrays. If there are no more 
            elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

TestCases:
    For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() 
    repeatedly should output 1, 2, 3, 4, 5, 6.
    

Time Complexity:
    O(nm) where n is the length of outer array and 
                m is the legth of max(inner array)
    O(X) wher X is total numbers in the 2D array
    next() - O(1)
    has_next() - O(1)
Space Complexity:
    O(nm) - store the 2D Array
"""


class TwoDIterator:
    def __init__(self, array):
        self.array = array
        # Keep track of last element that was returned. so that next time
        # start with the next element. This reduces time complexity
        self.lastElemIdx = (0, -1)
        self.lenArr = len(self.array)

    def next(self):
        try:
            outer, inner = self.lastElemIdx
            if self.has_next():
                for i in range(outer, self.lenArr):
                    arr = self.array[i]
                    if not arr:
                        continue
                    for j in range(inner + 1, len(arr)):
                        self.lastElemIdx = (i, j)
                        return arr[j]
                    inner = -1
            raise IndexError
        except IndexError:
            return "Index out of range"

    def has_next(self):
        outer, inner = self.lastElemIdx
        for i in range(outer, self.lenArr):
            arr = self.array[i]
            if not arr:
                continue
            for j in range(inner + 1, len(arr)):
                return True
            inner = -1
        return False


t = TwoDIterator([[1, 2], [3], [], [4, 5, 6]])

print(t.next())
print(t.has_next())
print(t.next())
print(t.has_next())
print(t.next())
print(t.has_next())
print(t.next())
print(t.has_next())
print(t.next())
print(t.has_next())
print(t.next())
print(t.has_next())
print(t.next())
