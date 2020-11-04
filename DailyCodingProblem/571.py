"""
No: 571
Date: 11-04-2020

Problem:
    Tower of Hanoi
    The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

    All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

    The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

    You can only move one disk at a time.
    A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
    You cannot place a larger disk on top of a smaller disk.
    Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.


TestCases:
    For example, with n = 3, we can do this in 7 moves:
        Move 1 to 3
        Move 1 to 2
        Move 3 to 2
        Move 1 to 3
        Move 2 to 1
        Move 2 to 3
        Move 1 to 3
    

Time Complexity:
    O(n) where n is number of discs
Space Complexity:
    O(2n) recurring n times
Odd - C should be Aux in start
Even - B should be Aux in start
"""


def TowerOfHanoi(n, a, b, c):
    if not n:
        return
    TowerOfHanoi(n - 1, a, c, b)
    print("Move ", a, " to ", c)
    TowerOfHanoi(n - 1, b, a, c)
    pass


TowerOfHanoi(2, 1, 2, 3)

