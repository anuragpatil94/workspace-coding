"""
No: 26
Date: 11-30-2020

Problem:
    Create a class CallCounter that tracks the number of calls a client has made 
    within the last 3 seconds. Your class should contain one method, ping(int t) 
    that receives the current timestamp (in milliseconds) of a new call being 
    made and returns the number of calls made within the last 3 seconds.
    Note: you may assume that the time associated with each subsequent call to 
    ping is strictly increasing.

TestCases:
    ping(1), return 1 (1 call within the last 3 seconds)
    ping(300), return 2 (2 calls within the last 3 seconds)
    ping(3000), return 3 (3 calls within the last 3 seconds)
    ping(3002), return 3 (3 calls within the last 3 seconds)
    ping(7000), return 1 (1 call within the last 3 seconds)

Time Complexity:
    
Space Complexity:
    
"""


class CallCounter:
    def __init__(self):
        self.arr = []
        pass

    def ping(self, ts):
        self.arr.append(ts)
        count = 0
        for num in range(len(self.arr) - 1, -1, -1):
            if ts - self.arr[num] <= 3000:
                count += 1
            else:
                break
        print(count)
        self.arr = self.arr[num:]


c = CallCounter()

c.ping(1)
c.ping(300)
c.ping(3000)
c.ping(3002)
c.ping(7000)
