def SumSquareDifference(n):
    ''' 
        Time Complexity: O(n)
        Space Complexity: O(1)
    '''
    SumOfSquares = 0
    SumOfNumbers = 0
    for num in range(1, n+1):
        SumOfNumbers = SumOfNumbers + num
        SumOfSquares = SumOfSquares + (num*num)
    return (SumOfNumbers*SumOfNumbers)-SumOfSquares
    pass


def BS_SumSquareDifference(n):
    ''' Patterns:
            These 2 examples create 2 patterns
            1) Sum of numbers - [n(n+1)/2]
            2) Sum of Squares - [n(n+1)(2n+1)/6]
        Time Complexity: O(1)
        Space Complexity: O(1)
    '''
    return int(((n*(n+1)/2) * (n*(n+1)/2)) - (n*(n+1)*((2*n)+1)/6))

    pass


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(SumSquareDifference(number))
    print(BS_SumSquareDifference(number))
