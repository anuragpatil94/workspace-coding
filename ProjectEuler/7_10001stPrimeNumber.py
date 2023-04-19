import math


def isPrime(num):
    if(num < 2):
        return False
    if(num % 2 == 0):
        return num == 2
    if(num % 3 == 0):
        return num == 3

    sqrtNum = math.sqrt(num)
    i = 5

    while(i <= sqrtNum):
        if num % i == 0 or num % (i+2) == 0:
            return False
        i = i+6
    return True


def findPrime(L):
    ''' This Solution is O(sqrt(n))'''
    # L - Lth Number
    num = 0
    primeCounter = 0
    primeNumber = 0
    while(primeCounter != L):
        isNumPrime = isPrime(num)
        if(isNumPrime):
            primeCounter += 1
            if (primeCounter == L):
                primeNumber = num

        num += 1
    return primeNumber


if __name__ == "__main__":
    print(findPrime(10001))
