"""
No: 252
Date: 10-09-2021

Problem:
  Meeting Rooms

TestCases:
  

Time Complexity:
  n log n
Space Complexity:
  1
"""


class MeetingRooms:
    def __init__(self):
        pass

    def main(self, intervals):
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


m = MeetingRooms()

print(m.main([[5, 10], [0, 30], [15, 20]]))
print(m.main([[7, 10], [2, 4]]))
