"""
No: 
Date: 10-04-2021

Problem:
  You are given a two-dimensional matrix, grid, containing only ones and zeroes 
  where zeroes represent land and ones represent water. An “island” is a group 
  of one or more contiguous zeroes connected four-directionally 
  (i.e. up, down, left and right). A magical island is an island that is 
  completely surrounded by water on all sides four-directionally. 
  Return the total number of magical islands in the grid.


TestCases:
  Ex: Given the following grid…

  grid = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
  ], return 1.
  Ex: Given the following grid…

  grid = [
    [1, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0]
  ], return 1 
  (the island in the right-most column is not entirely surrounded by water to 
  its right for example).

Time Complexity:
  
Space Complexity:
  
"""


class MagicalIslands:
    def __init__(self):
        pass

    def recur(self, matrix, visited, current):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = current[0]
        j = current[1]
        visited[i][j] = 1
        for direction in directions:
            newI = i + direction[0]
            newJ = j + direction[1]
            if 0 <= newI < len(matrix) and 0 <= newJ < len(matrix[j]):
                # Found Land and not Visited
                if not visited[newI][newJ] and not matrix[newI][newJ]:
                    return self.recur(matrix, visited, (newI, newJ))
        return True
        pass

    def solution(self, matrix):
        visited = [[0] * len(matrix[0])] * len(matrix)
        print(visited)
        ans = 0
        for i in range(1, len(matrix) - 1):
            for j in range(1, len(matrix[i]) - 1):
                if not matrix[i][j] and not visited[i][j]:
                    if self.recur(matrix, visited, (i, j)):
                        ans += 1
        print(ans)


m = MagicalIslands()
m.solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
m.solution([[1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0]])
