"""
No: 27
Date: 11-30-2020

Problem:
    Design a class, MovingAverage, which contains a method, next that is 
    responsible for returning the moving average from a stream of integers.

    Note: a moving average is the average of a subset of data at a given 
    point in time.



TestCases:
     i.e. the moving average has a capacity of 3.
    MovingAverage movingAverage = new MovingAverage(3);
    m.next(3) returns 3 because (3 / 1) = 3
    m.next(5) returns 4 because (3 + 5) / 2 = 4 
    m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
    m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6

Time Complexity:
    
Space Complexity:
    
"""


class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.arr = []
        self.avg = 0
        pass

    def next(self, val):
        avg = self.avg
        if len(self.arr) + 1 > 3:
            x = self.arr.pop(0)
            self.arr.append(val)
            avg = (avg - self.arr[0] + (3 * self.arr[2])) / 3
        else:
            self.arr.append(val)
            avg = sum(self.arr) / len(self.arr)
        print(avg)
        self.avg = avg
        return avg


m = MovingAverage(3)
m.next(3)
m.next(5)
m.next(8)
m.next(6)
