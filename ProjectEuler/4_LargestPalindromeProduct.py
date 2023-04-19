import time

def isLargestPalindromeProduct():
    ''' Time Complexity O(n^2). This is the best possible time.'''
    max = 0
    for num1 in range(999,99,-1):
        if(num1%11 == 0):
            b = 999
            db = 1
        else:
            b = 990
            db = 11
        for num2 in range(b,99,-db):
            if(num1*num2 > max and isPalindrome(num1*num2) and num1*num2 > max):
                max = num1*num2
    print(max)

def isPalindrome(number):
    ''' Time Complexity O(k) where k is number of integers in the number '''
    strnum      = str(number)
    length      = len(strnum)
    endPointer  = len(strnum) - 1 
    isPalindrome = False

    for startPointer in range(0, length//2):
        if strnum[startPointer] != strnum[endPointer]:
            isPalindrome = False
            break
        isPalindrome = True
        endPointer = endPointer - 1
    return isPalindrome

if __name__ == "__main__":
    start = time.process_time()
    isLargestPalindromeProduct()
    print(time.process_time() - start)