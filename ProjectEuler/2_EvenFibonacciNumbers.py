def sumEvenFibonacciNumbers(limit):
    ''' Time Complexity = O(k) where k is kth element which is less than limit '''
    num1 = 1
    num2 = 2
    sum = 0
    while num2 <= limit:
        if num2 % 2 == 0:
            sum = sum + num2
        temp = num2
        num2 = num1 + num2
        num1 = temp
    return sum


def BS_sumEvenFibonacciNumbers(limit):
    ''' Time Complexity = O(k) where k is kth element which is less than limit. This is because every 3rd number in Fibonacci series is even, reducing number of iterations.'''
    num1 = 1
    num2 = 1
    num3 = num1 + num2
    sum = num3
    while num3 + num2 <= limit:
        num1 = num3 + num2
        num2 = num1 + num3
        num3 = num1 + num2
        sum = sum + num3
    return sum


if __name__ == "__main__":
    print(sumEvenFibonacciNumbers(4000000))

    # Best Solution
    print(BS_sumEvenFibonacciNumbers(4000000))
    pass
