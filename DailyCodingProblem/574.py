"""
No: 574
Date: 11-08-2020

Problem:
    Implement a bit array.

    A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.

TestCases:

Time Complexity:
    O(1) - get and set methods
Space Complexity:
    O(n) - n is initial size of bitarray 
"""


class BitArray:
    def __init__(self, size):
        self.array = [0] * size
        self.size = size

    def set(self, index, val) -> None:
        if not (0 <= val <= 1 and isinstance(val, int)):
            raise ArithmeticError()
        if 0 <= index < self.size:
            self.array[index] = val
        else:
            raise IndexError()
        pass

    def get(self, index) -> int:
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError()


a = BitArray(5)
a.set(2, 1)
print(a.get(1))

